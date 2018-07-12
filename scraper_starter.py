'''
short snippet which starts some script with selenium using chrome as browser and after some time it kill all browser, process and so on
'''
import time
import psutil
from subprocess import Popen

p = Popen(['python','YOUR SCRIPT.PY'])
time.sleep(TIME IN SECONDS)

p.kill()
processes = [item for item in psutil.process_iter()]
chrome = [item for item in processes if 'rome' in item.name()]
[item.kill() for item in chrome]






