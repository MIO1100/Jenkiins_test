import requests
r = requests.get("http://localhost:8000/")
if r.status_code == requests.codes.ok:
    print("Test OK")
else: raise Exception("ERROR")
