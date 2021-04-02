import subprocess
import time

process = subprocess.call("python3 manage.py runserver")

time.sleep(10)

test = subprocess.call("python3 tests/test.py")
