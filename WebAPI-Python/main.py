from fastapi import FastAPI
from starlette.requests import Request
from pydantic import BaseModel
# import inferModel.infer as infer

app = FastAPI()

@app.get("/")
def root(request: Request):
    return {"AAA": 3}