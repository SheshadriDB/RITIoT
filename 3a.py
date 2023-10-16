#switching multiple LED based on LDR reading with Raspberry pi
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
  x.output(LIGHT_PIN2,False)
else:
  x.output(LIGHT_PIN1,False)
  x.output(LIGHT_PIN2,True)
