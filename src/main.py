from fastapi import FastAPI, status
app = FastAPI()

@app.get("/api/hello_world",status_code=status.HTTP_201_CREATED)
async def hello_world():
    return {"message": "Hello World"}