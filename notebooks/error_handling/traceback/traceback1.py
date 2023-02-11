import logging
import sys
import requests
import traceback
import os

logging.basicConfig(filename = "debug.log", 
            level = os.environ.get("LOGLEVEL", "INFO").upper(),
            format = '%(asctime)s %(levelname)s %(filename)s:%(lineno)s - %(funcName)s(): %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S') 

logger = logging.getLogger()

if __name__ == "__main__":

    url = "http://thisurlprobablydoesntexist.com"

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        logger.exception("Connection Error")
        print(traceback.format_exc()) # doing the same thing as logger.exception("")
        print(-1, 'Connection Error')
    else:
        print(response.status_code, response.content)
