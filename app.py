# import the fastapi library

from fastapi import FastAPI

# create an instance object of the fastAPI class

app = FastAPI()

# decorator

@app.get("/")

def home():
    return {"message": "come back to the chat room"}



