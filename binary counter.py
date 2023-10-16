#assignment1
#3 BIT BINARY COUNTER 
import RPi.GPIO as x
import time
pin=[16,20,21]
x.setmode(x.BCM)
for p in pin:
  x.setup(p,x,OUT)
  try:
    while True:
      for i in range (8):
        x.output(pin[0], i & 0x1)
        x.output(pin[1], i & 0x2)
        x.output(pin[2], i & 0x4)
        time.sleep(2)
  except KeyboardInterrupt:
    x,cleanup()
    exit()
