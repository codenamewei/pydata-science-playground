
import boto3
import time
import os
from multiprocessing import Pool, cpu_count
from typing import List
import json
import sys
import threading

filename = r"C:\Users\codenamewei\Documents\xboxgamebar\Captures\disney.mp4"
bucketname = "hello-world-abc"
basename = os.path.basename(filename)
sizeperchunk = 10000000# roughly 10 mb parts

configfilepath = r"C:\Users\codenamewei\Downloads\temp\awscredential.json"

"""
greyanatomy2.mp4 31MB
by single process:  33.51532959938049s
by multiple worker: 32.281418800354004s

disney.mp4 225MB
by single process:  152.05219435691833s
by multiple worker: 127.70767831802368s
"""

        
#(param : dict) -> dict:
def worker_upload_file(param : dict) -> dict:
    """
    (KEY) aws_access_key_id <> value : str
    (KEY) aws_secret_access_key <> value : str
    (KEY) bucketname <> value : str
    (KEY) objectname <> value : str
    (KEY) uploadid <> value : int
    (KEY) partnumber <> value : int
    (KEY) contents <> value : bytes
    """

    s3resource = boto3.resource('s3', aws_access_key_id=param["aws_access_key_id"], aws_secret_access_key= param["aws_secret_access_key"])
    
    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#multipartuploadpart
    uploadPart = s3resource.MultipartUploadPart(
        bucket_name = param["bucketname"], object_key = param["objectname"], multipart_upload_id = param["uploadid"], part_number = param["partnumber"])

    uploadPartResponse = uploadPart.upload(
        Body=param["contents"],
    )

    #progress(sys.getsizeof(piece))
    print(f'Completed part {param["partnumber"]}')
    
    return {'PartNumber': param["partnumber"], 'ETag': uploadPartResponse['ETag']}
        
if __name__ == "__main__":
    
    #declare s3client
    with open(configfilepath, 'r') as openfile:
 
        # Reading from json file
        config = json.load(openfile)

        s3client = boto3.client('s3', aws_access_key_id=config["aws_access_key_id"], aws_secret_access_key= config["aws_secret_access_key"])
    
    
     #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_multipart_upload
    multipart_upload = s3client.create_multipart_upload(
        ACL='private',
        Bucket=bucketname,
        ContentType='video/mp4',
        Key=basename,
    )

    part_number = 1
    parts = []

    filechunkbase = {"aws_access_key_id": config["aws_access_key_id"], 
                     "aws_secret_access_key": config["aws_secret_access_key"], 
                     "bucketname": bucketname, 
                     "objectname": basename}

    start = time.time()

    fileidcounter = 1
    filechunks : list = []

    with open(filename, 'rb') as f:
        while True:
            piece = f.read(sizeperchunk) 
            if piece == b'':
                break
            else:

                thisfilechunk = filechunkbase.copy()
                thisfilechunk["uploadid"] = multipart_upload['UploadId']
                thisfilechunk["partnumber"] = fileidcounter
                thisfilechunk["contents"] = piece
                filechunks.append(thisfilechunk)

                fileidcounter += 1

    parts = []

    #Using as much of workers as per the number of chunks
    WORKERS = len(filechunks) if (cpu_count() > len(filechunks)) else cpu_count() 
    print(f"Using {WORKERS} multiprocessing workers\n")

    #filechunks = list(range(0, WORKERS))

    with Pool(WORKERS) as p:

        for result in p.imap(worker_upload_file, filechunks):
            parts.append(result)
    
    ## To signal completion

    completeResult = s3client.complete_multipart_upload(
    Bucket=bucketname,
    Key=basename,
    MultipartUpload={
        'Parts': parts
    },
    UploadId=multipart_upload['UploadId'],)

    end = time.time()

    print(f"Time consumed in seconds: {end - start}s")