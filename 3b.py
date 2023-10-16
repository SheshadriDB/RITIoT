#switching multiple LEDS with different delays on LDR reading with raspberrypi
import RPi.GPIO as x
import time
x.setwarnings (False)
x.cleanup()
x.setmode(x.BCM)
LDR_PIN=26
LIGHT_PIN1=18
LIGHT_PIN2=19
x.setup(LIGHT_PIN1,x.OUT)
x.setup(LIGHT_PIN2,x.OUT)
x.setup(LDR_PIN,,x.IN)
while True:
  if (x.input(LDR_PIN)==1)
  x.output(LIGHT_PIN1,True)
  time.sleep(2)
  x.output(LIGHT_PIN2,False)
else:
  x.output(LIGHT_PIN2,True)
  time.sleep(3)
  x.output(LIGHT_PIN1,False)
