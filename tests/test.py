import requests
r = requests.get("http://localhost:8000/",verify=False)
if r.status_code == requests.codes.ok:
    print("Test OK")
else: raise Exception("ERROR")
