#interface ldr sensor raspberry pi and write a program to turn on LED at semsor detections
import RPi.GPTIO as x
import time
x.setwarnings(False)
x.cleanup()
x.setmode(x.BCM)
LDR_PIN=26
LIGHT_PIN1=2
x.setup(LIGHT_PIN1,x.OUT)
x.setup(LDR_PIN,x.IN)
while True:
  if(x.input(LDR_PIN)==1):
    xA.output(LIGHT_PIN1,True)
  else:
    x.output(LIGHT_PIN1,False)
