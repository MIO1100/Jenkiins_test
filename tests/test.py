import requests
import time

page = requests.get("http://localhost:8000/")
time.sleep(5)

if page.status_code == requests.codes.ok:
    print ("OK")
else: print("error")

