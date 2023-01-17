from multiprocessing import Pool, cpu_count
from datetime import datetime
from random import randint;
import os
import time

def worker(param : dict) -> str:
    """
    (KEY) 0 : file_id
    (KEY) 1 : file_str
    """
    now = datetime.now()
    date_in_str = now.strftime("%Y-%H-%d %H:%M:%S")
    
    fileid = param[0]
    filename = param[1]

    # Do some operation
    print(f"{date_in_str}: Do some work: File ID {fileid}: {os.path.basename(filename)}")

    time.sleep(randint(0, 10))

    now = datetime.now()
    date_in_str = now.strftime("%Y-%H-%d %H:%M:%S")

    print(f"{date_in_str}: Done: {os.path.basename(filename)}")
    return True

if __name__ == "__main__":

    filelist = []
    rootpath = r"C:\Users\codenamewei\Documents\nlp-meeting-data\text"

    filelist = list(map(lambda x:  os.path.join(rootpath, x), os.listdir(rootpath)))
    filelist = filelist[0: 2]
    
    file_id = list(range(0, len(filelist)))
                   
    zippedparam = zip(file_id, filelist)

    WORKERS = cpu_count()
    print(f"Using {WORKERS} multiprocessing workers\n") #Maps to the number of cores in a node

    buffer = []
    with Pool(WORKERS) as p:
        
        for result in p.imap(worker, zippedparam):
            buffer.append(result)
