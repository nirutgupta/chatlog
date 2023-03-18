Code written in Python3.10

Libraries used

fastAPI
pydantic

## Database
Currently in memory database is getting used

## How to run the app on localhost
Install dependencies
$ pip install -r requirements.txt

Run
$ uvicorn api.routes:app

$ open http://127.0.0.1:8000/v1/chatlogs#/
