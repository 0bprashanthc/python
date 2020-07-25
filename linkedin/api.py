import requests
import json
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url,headers=dict())
    print(response.status_code, response.text)
    response_json = json.loads(response.text)
    print(response_json)
