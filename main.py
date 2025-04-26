from fastapi import  FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"message":"Hello World"}

from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# ENV values
DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/init/table")
def create_users_table():
    print("11")
    try:
        print(DATABASE_URL)
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        # Create table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            phone VARCHAR(20),
            address TEXT,
            city VARCHAR(50),
            state VARCHAR(50),
            country VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Table 'users' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail={f"str(e)={str(e)}, message={e.__str__()}"})
