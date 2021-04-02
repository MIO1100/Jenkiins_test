import subprocess
import time


process = subprocess.Popen(['python3', 'manage.py','runserver'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


time.sleep(10)
test = subprocess.Popen(['python3', 'tests/test.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

