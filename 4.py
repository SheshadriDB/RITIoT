#interface DHT11 sensor with Raspberry Pi and print TEMP AND HUMIDITY
import time
import board
import adafruit_dht
import psutil
for proc in psutil.process_iter():
  if proc.name()=='libgpiod_pulsein' or proc.name()=='libgpiod_pulsei':
    proc.kill()
    sensor=adafruit_dht.DHT11(board.D4)
    while True:
      try:
        temp=sensor.temperature
        humidity=sensor.humidity
        print("Tempersture: {}*C Humidity: {}% ".format(temp,humidity0)
              except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
      except Exception as error:
        sensor.exit()
        raise error
        time.sleep(2.0)

