from fastapi import FastAPI
import inferModel.infer as Infer

app = FastAPI()

@app.get("/")
async def root(url: str = None):
    if url == None:
        return {"Error":"url is None!"}
    else:
        w2i = Infer.wordStr2IntVec()
        result = 0 if Infer.infer(url, w2i)[0]== "good" else 1
        return {"result": result}
