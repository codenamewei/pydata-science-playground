import sys
import requests

try:
    response = requests.get(sys.argv[1])
    
except requests.exceptions.ConnectionError:
    print(-1, 'Connection Error')
else:
    print(response.status_code, response.content)