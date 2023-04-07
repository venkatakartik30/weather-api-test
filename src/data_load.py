import os
import dask.dataframe as ddf
from sqlalchemy import create_engine

def data_process(directory):
    db_engine = get_engine()
    df = compute_dataframe(directory)
    # Concatenate all df 
    file_d= more_compute(df)
    # Get rid of any rows with  missing temp data and percp data
    result = file_d[(file_d['max_temp'] != -9999) |
                  (file_d['min_temp'] != -9999) | (file_d['precipitation'] != -9999)]
    result = result_compute(result,file_d)
    result.rename(columns={'max_temp': 'AvgMaxtemp', 'min_temp': 'AvgMintemp',
               'precipitation': 'TotalAccPrecipitation'}, inplace=True)
    write_data(file_d,db_engine,result)

def get_engine():
    return create_engine('sqlite:///data_base.db', echo=True)

def compute_dataframe(directory):
    return  [
    (ddf.read_csv(os.path.join(directory, file_d), sep="\t", header=None,
                  names=["date", "max_temp", "min_temp", "precipitation"])
     .assign(Station_ID=file_d[:11]))
    for file_d in os.listdir(directory) if file_d.endswith(".txt")
    ]

def more_compute(df):
    fd = ddf.concat(df)
    fd = fd.compute()
    fd = fd.reset_index(drop=True)
    return fd

def result_compute(result,file_d):
    return result.groupby(['Station_ID', file_d['date'].map(str).str[:4]]).agg({
        'max_temp': 'mean',
        'min_temp': 'mean',
        'precipitation': 'sum'
    }).reset_index()

def write_data(file_d,db_engine,result):
    db_session = db_engine.raw_connection()
    # Make changes in the weather file_d to a table in the database
    file_d.to_sql("record_weather", db_session, if_exists="replace",
                index=True, index_label='id')
    result.to_sql("stat_weather", db_session, if_exists="replace",
                  index=True, index_label='id')
    db_session.commit()
    db_session.close()


data_process('../wx_data')
