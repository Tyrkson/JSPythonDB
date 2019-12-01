from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import db
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CollectionName(BaseModel):
    name: str

class Element(BaseModel):
    name: str
    element: str

class User(BaseModel):
    email: str

class UserCredentials(BaseModel):
    email: str
    password: str

@app.get("/")
def read_root():
    return db.testdb()

@app.get("/delete")
def read_root():
    return db.deleteCollections()

@app.post("/addElement")
def addElement(item: Element):
    return db.addElement(item.name, item.element)

@app.post("/get")
def getC(item: CollectionName):
    return db.getCollection(item.name)

@app.post("/getUser")
def getUser(item: User):
    return db.getUser(item.email)

@app.post("/checkUser")
def getUser(item: UserCredentials):
    return db.checkUserCredentials(item.email, item.password)
