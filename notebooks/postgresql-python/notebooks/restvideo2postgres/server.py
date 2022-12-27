from fastapi import FastAPI, UploadFile
from typing import Union
import os
import psycopg 
import base64
import time

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



@app.put("/video")
async def upload_video_file(videofile: UploadFile):
    """
    save video in the current function loop and return response once done
    """
    videoasbytes = await videofile.read()
    
    videodict = dict(filename = videofile.filename, content = base64.b64encode(videoasbytes))

    cur.execute("""INSERT INTO videostream (filename, content) VALUES (%(filename)s, %(content)b)""", videodict) 
    
    
    print(f"Time consumed in seconds: {end - start}s")
    
    return {"issuccess": True}

@app.get("/video/{id}")
async def retrieve_video(id: str):
        
    cur.execute("SELECT content FROM videostream WHERE id = %(id)s", dict(id = id))

    videoasbase64 = cur.fetchone()[0] # param[0] as bytes
    
    return {"contents": videoasbase64}
