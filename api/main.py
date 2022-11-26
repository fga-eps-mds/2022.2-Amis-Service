from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
#from database import engine, Base, get_db
#Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/api/hello_world",status_code=status.HTTP_201_CREATED)
async def hello_world():
    return {"message": "Hello World"}