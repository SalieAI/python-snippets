'''
Date: August 2018
Short script with CLI to be used for restarting others scripts 
Restarter will first try to run choosen script with python3, if that will be unsuccesful will try to run with python
which can be on most system python2
'''
import argparse
import logging
from subprocess import Popen
import time

logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--script', action="store", dest="script", help = 'name of script, e.q. : helloworld.py')
parser.add_argument('-t', '--time', action="store", dest="time", type=int, help = 'duration of loop in seconds, e.g. 10')
settings = parser.parse_args()

def restarter(interval = settings.time, script = settings.script):
    '''
    starts script after defined interval of seconds will restart script and so on and so on
    infinite loop
    ============
    parameters:
        interval: time in seconds between start of script and killing of script, e.g. : 10
        script: name of script, e.q. : 'helloworld.py'
    '''
    logger.debug(f'Starting {settings.script} will restart in {settings.time} seconds and after that there will be infinite loops with duration of {settings.time} seconds')
    while True:
        try:
            p = Popen(['python3', script])
        except:
            p = Popen(['python', script])
        time.sleep(interval)
        p.kill()
    
if __name__ == "__main__":
    restarter()
