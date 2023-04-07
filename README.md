# API Weather

    - available at this endpint : http://127.0.0.1:8000/docs


## Installation and Usage

    python -m venv virtual_env

### To activate the virtual environment:

    virtual_env\Scripts\activate (in Windows)
    source virtual_env/bin/activate (in Linux and Mac)

### Required dependencies:

    pip install -r requirements.txt

### Move to src dir:
    
    cd src

### To ingest the data:

    python data_load.py

### To run the server:

    uvicorn app:app --reload

### Tests

    cd src 
    python data_load.py
    pytest
    
# AWS Deployment

    - Deployment to aws can be done through various services available in aws cloud platform , for example an EC2 instance can be used to do same.

