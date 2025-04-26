import os

from sqlalchemy import MetaData, create_engine
from dotenv import load_dotenv

from databases import Database
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
database = Database(DATABASE_URL)

metadata = MetaData()

engine = create_engine(DATABASE_URL)