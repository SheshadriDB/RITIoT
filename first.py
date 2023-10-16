import RPi.GPIO as X
import time 
pin=18
X.setmode(x.BCM)
X.setup(pin,X.OUT)
try:
  while True:
    X.output(pin,True)
    time.sleep(2)
    X.output(pin,False)
    time.sleep(2)
except KeyboardInterrupt:
  X.cleanup()
  exit()
