import requests
r = requests.get("http://127.0.0.1:8000/")
if r.status_code == requests.codes.ok:
    print("Test OK")
else: raise Exception("ERROR")
