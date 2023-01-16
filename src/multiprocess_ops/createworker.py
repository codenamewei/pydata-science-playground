from multiprocessing import Pool, cpu_count
from datetime import datetime
from random import randint;
import os
import time

def worker(filename: str) -> str:

    now = datetime.now()
    date_in_str = now.strftime("%Y-%H-%d %H:%M:%S")

    # Do some operation
    print(f"{date_in_str}: Do some work: {os.path.basename(filename)}")

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

    WORKERS = cpu_count()

    worker_id_list = list(range(0,  WORKERS))
    print(f"Number of workers: {WORKERS}") #Maps to the number of cores in a node

    print(f"Using {WORKERS} multiprocessing workers\n")

    buffer = []
    with Pool(WORKERS) as p:

        for result in p.imap(worker, filelist):
            buffer.append(result)
