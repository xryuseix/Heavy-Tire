from fastapi import FastAPI
from pydantic import BaseModel
import inferModel.infer as infer

app = FastAPI()

@app.get("/")
def main(key: Key):
    return {"AAA":3}