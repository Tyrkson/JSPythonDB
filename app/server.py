from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import db

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

@app.get("/")
def read_root():
    return db.testdb()

@app.post("/addElement")
def ax_25(item: Element):
    return None

@app.post("/get")
def ax_25(item: CollectionName):
    return None
