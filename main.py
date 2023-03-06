from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def hello():
    return {"Hello World"}