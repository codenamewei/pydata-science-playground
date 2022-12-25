from fastapi import FastAPI, UploadFile
from typing import Union
import os
import psycopg 
import base64

"""
Start server with 
uvicorn server:app --reload
"""

app = FastAPI()


# connect to an existing database
# https://www.psycopg.org/psycopg3/docs/api/connections.html#psycopg.Connection.execute
conn = psycopg.connect(
    user="postgres",
    password="password",
    host="database.cosqamqjez6h.ap-northeast-2.rds.amazonaws.com",
    port='5432',
    autocommit = True
)

# open a cursor to perform database operations
cur = conn.cursor()

@app.put("/image")
async def upload_image(imagefile: UploadFile):
    """
    save video in the current function loop and return response once done
    """
    
    imageasbytes = await imagefile.read()

    imagedict = dict(filename = imagefile.filename, content = imageasbytes)

    cur.execute("""INSERT INTO album (filename, content) VALUES (%(filename)s, %(content)b)""", imagedict) 
    
    return {"issuccess": True}

@app.get("/image/{filename}")
async def retrieve_image(filename: str):

    cur.execute("SELECT content FROM album WHERE filename = %(filename)s", dict(filename = filename))

    imageasbytes = cur.fetchone()[0] # param[0] as bytes
    
    imageasbase64 = base64.b64encode(imageasbytes)
    
    return {"contents": imageasbase64}
