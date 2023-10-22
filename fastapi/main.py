from typing import Union

from fastapi import FastAPI,APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from pymongo import MongoClient
from passlib.context import CryptContext
from search import ask
from models import User, Report
from models.User import UserData
from models.Report import ReportData
from database import add_admin
from fastapi.encoders import jsonable_encoder
from routers import router as routers

config = dotenv_values(".env")

hash_helper = CryptContext(schemes=["bcrypt"])

app = FastAPI()

app.include_router(routers, prefix="/api")


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
