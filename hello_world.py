import sys
import uuid
import os
import datetime
import base64

import uvicorn
from fastapi import FastAPI, HTTPException, status, Request, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from pprint import pprint


#create app
app = FastAPI(title='Test')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/") 
async def root(): 
    return {"message": "Hello Anh Vi"}


@app.post("/input")
async def get_body(request: Request):
    data = await request.json()
    pprint(data)
    return "OK"
    # return await request.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9452)
