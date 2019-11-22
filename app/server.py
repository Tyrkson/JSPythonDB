import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI()

class ExternalMsg(BaseModel):
    name: str


def randomNumber(sat):
    return sat + str(random.randint(0,9))



@app.get("/")
def read_root():
    return "Hello world"

@app.post("/decode")
def ax_25(item: ExternalMsg):
    return None

@app.options("/")
def wtf():
    return "Hello world"
