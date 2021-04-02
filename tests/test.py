import requests
import time

page = ''
while page == '':
    try:
        page = requests.get("http://localhost:8000/")
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue
if page.status_code == requests.codes.ok:
    print("Test OK")
else: raise Exception("ERROR")
