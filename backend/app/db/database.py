
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb+srv://prakharverma2209_db_user:HG2FDL1obfOa5Pea@cluster0.9vfmt7u.mongodb.net/?appName=Cluster0")
db = client["userdata"]
collection = db["user"]