#remove \xe2\x98\x81
import requests
import json
# Making a GET request DON'T ADD PARENTHETICALLS AROUND CONTENT
r = requests.get('https://clouddata.scratch.mit.edu/logs?projectid=544007050&limit=1&offset=0')

r.raise_for_status()  # raises exception when not a 2xx response
if r.status_code != 204:
    print(r.json())
    b = str(r.json())
    a = b.replace("'", '"')
    a = json.loads(a)
    for i in a:
        print(i["value"])
