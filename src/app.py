from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import create_engine, text
from sql.sql import compute


engine = create_engine('sqlite:///data_base.db', echo=True)


app = FastAPI()

def compute_filter(date,station_id):
    filters = [f"Date == '{date}'"] if date else []
    filters += [f"Station_ID == '{station_id}'"] if station_id else []
    return filters

def process_records(query):
    with engine.connect() as conn:
        rows = conn.execute(text(query)).fetchall()
        if not rows:
            raise HTTPException(
                status_code=404, detail="No data found for the specified dates")
        weather_data = [{"station_id": row[5],
                         "date": row[1],
                         "max_temp": row[2],
                         "min_temp": row[3],
                         "precipitation": row[4]} 
                         for row in rows 
                         ]
    return weather_data

def process_stats(query):
    with engine.connect() as conn:
        rows = conn.execute(text(query)).fetchall()
        if not rows:
            raise HTTPException(
                status_code=404, detail="No data found for the specified dates")
        weather_data = [{"station_id": row[1], 
                         "date": row[2], 
                         "avg_max_temp": row[3], 
                         "avg_min_temp": row[4], 
                         "total_acc_precipitation": row[5]} 
                         for row in rows
                        ]
    return weather_data

@app.get("/api/weather/")
def get_weather_data(date: str = Query(None), station_id: str = Query(None),
                         page: int = Query(1), size: int = Query(10)):
    '''
    @params: date ,station_id, page ,size
    @feature: get weather records
    '''
    offset = (page - 1) * size
    filters=compute_filter(date,station_id)
    query=compute(filters,size,offset,"record_weather")
    weather_data=process_records(query)
    return weather_data


@app.get("/api/weather/stats")
def get_weather_stats(year: str = Query(None), station_id: str = Query(None),
                       page: int = Query(1), size: int = Query(10)):
    '''
    @params: year ,station_id, page ,size
    @feature: get weather stats
    '''
    offset = (page - 1) * size
    filters=compute_filter(year,station_id)
    query=compute(filters,size,offset,"stat_weather")
    weather_data=process_stats(query)
    return weather_data
