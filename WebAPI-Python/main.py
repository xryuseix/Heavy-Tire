from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import inferModel.infer as Infer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
async def root(url: str = None):
    if url == None:
        return {"Error":"url is None!"}
    else:
        w2i = Infer.wordStr2IntVec()
        result = 0 if Infer.infer(url, w2i)[0]== "good" else 1
        return {"result": result}

# uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8080
# http://localhost:8080