#motor relay to operate in both directions clockwise abd anticlockwise rotation using two relay module
import RPi.GPIO as x
import time
x.setwarnings(False)
x.cleanup()
x.setmode(x.BCM)
pin1=22
x.setup(pin1,x.OUT)
while true:
  try:
    x.output(pin1,True)
    time.sleep(4)
    x.output(pin1,False)
    time.sleep(5)
   except:
    time.sleep(10)
    continue
