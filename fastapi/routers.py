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


router = APIRouter()
@router.get("/")
async def root():
    return {"message": "API using Fast API and pymongo"}


@router.post("/login")
def admin_login(request: Request, admin_credentials : UserData = Body(...)):
    admin_credentials = jsonable_encoder(admin_credentials)
    admin_exists = request.app.database["users"].find_one({
        "email": admin_credentials['email']
    })
    print(admin_exists)
    print(admin_credentials)
    if admin_exists and (admin_credentials['password'] == admin_exists['password']):
        print("logged in")
        return "Login successful! Welcome "+admin_exists['fullname']
    print("User does not exist. Please register.")
    return "User does not exist. Please register."


@router.post("/register")
def admin_signup(request: Request, admin: UserData = Body(...)):
    print(admin)
    admin = jsonable_encoder(admin)
    print(admin)
    admin_exists = request.app.database["users"].find_one({
        "email": admin['email']
    })
    if admin_exists:
        print("User already exists")
        return "User already exists"
    
    new_admin = request.app.database["users"].insert_one(admin)
    if new_admin:
        return "Registered successfully! Head to the Login page."
    return "Opps! Error occurred!"


@router.post("/submit")
def submit(request: Request, report: ReportData = Body(...)):
    print(report)
    report = jsonable_encoder(report)
    print(report)
    new_report = request.app.database["report"].insert_one(report)
    if new_report:
        return "Submitted successfully! We got you!"
    return "Opps! Error occurred!"

@router.get("/ask/{query}")
def get_response(query: str):
    return ask(query=query)

