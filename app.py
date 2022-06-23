from distutils.log import debug
from fastapi import FastAPI
import uvicorn
import subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World anand"}


if "__main__" == __name__:
    uvicorn.run("app:app")