from fastapi import FastAPI

app = FastAPI()

# setting up our API: to handle data. accept requests and return data

# needs to have @ decorator
@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"} # have to return Python Dictionaries because we work with JSON (format for dealing with data across the web)
