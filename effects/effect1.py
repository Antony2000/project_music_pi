import RPi.GPIO as GPIO
import time

arr_pin = [3,5,7,8,26,11,12,13,15,16,18]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

for x in arr_pin:
  GPIO.setup(x, GPIO.OUT)

for i in range(10):
    for x in arr_pin:
      GPIO.output(x, True)
    time.sleep(0.5)
    for x in arr_pin:
      GPIO.output(x, False)
    time.sleep(0.5)


