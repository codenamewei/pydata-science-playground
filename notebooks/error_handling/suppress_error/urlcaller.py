import sys
import requests

response = requests.get(sys.argv[1])

print(response.status_code, response.content)