from fastapi import  FastAPI
from fastapi import FastAPI, HTTPException
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# ENV values
DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
def index():
    return {"message": "Swapnil Bhau kay karu rayle"}

@app.get("/create")
def create():
    return {"message":"create successfully"}

@app.get("/get")
def create():
    return {"message":"fetch successfully"}

@app.get("/update")
def create():
    return {"message":"update successfully"}