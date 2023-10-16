#motor relay for on/off 
import RPi.GPIO as x
import time
x.setwarnings(False)
x.cleanup()
x.setmode(x.BCM)
pin1-22
x.setup(pin1,x.OUT)
try:
  while True:
    x.output(pin1,True)
    time.sleep(5)
    x.output(pin1,False)
    time.sleep(5)
except KeyboardInterrupt:
    x.cleanup()]
exit()
