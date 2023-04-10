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

    - Set up your source code repository, such as GitHub or AWS CodeCommit.
    - Create an RDS instance and configure it to store your ingested data.
    - Create an EC2 instance and configure it to run your FastAPI application.
    - Set up a CodeBuild project that clones your repository, installs any necessary dependencies, builds your application, and copies the built files to your EC2 instance.
    - Configure the CodeBuild project to run automatically whenever a new commit is pushed to your repository.
    - After the build process is complete, test your application to make sure it's running correctly on the EC2 instance.
    - If everything is working correctly, use a tool like AWS CodePipeline to automate the process of building and deploying your application to your EC2 instance.
    - Configure your FastAPI application to ingest data from a source and store it in your RDS instance.
    - Set up continuous monitoring and alerting for your application using tools like Amazon CloudWatch and AWS Lambda.
    - As your application evolves, continue to push changes to the repository and follow the same process to build and deploy to your EC2 instance with RDS.

