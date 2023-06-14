import uvicorn
from fastapi import FastAPI
from app.model import PostSchema

# Creating instance of fastapi class
app = FastAPI()


@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World"}
