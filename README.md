# comerciosempleados_fastapi

## Requirements
- Python 3.9
- Fastapi v0.75.1
- Uvicorn v0.17.6
- SQLAlchemy v1.4.36

## Installation of dependencies
### Virtual environment creation
1. `python3 -m venv <virtual_env_name>`  
2. `source <virtual_env_name>/bin/activate`

### Clone repository
1. `git clone git@github.com:mariomtzjr/comerciosempleados_fastapi.git`
2. `cd comerciosempleados_fastapi`
3. `pip3 install -r requirements.txt`

## Start server
1. `uvicorn main:app --port 9000`

Now server is running over `http://localhost:9000` or `http:127.0.0.1:9000`

## Endpoints
To know the endpoints, go to browser and type on url field: `http://localhost:9000/redoc`
