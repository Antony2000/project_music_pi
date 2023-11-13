import RPi.GPIO as GPIO
import time

arr_pin = [3,5,7,8,26,11,12,13,15,16,18,19,21,22,23,24]
arr_pin1 = [3,7,26,12,15,18,21,23]
arr_pin2 = [5,8,11,13,16,19,22,24]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

for x in arr_pin:
  GPIO.setup(x, GPIO.OUT)

for i in range(10):
    for x in arr_pin1:
      GPIO.output(x, True)
    for x in arr_pin2:
      GPIO.output(x, False)
    time.sleep(0.5)
    for x in arr_pin1:
      GPIO.output(x, False)
    for x in arr_pin2:
      GPIO.output(x, True)
    time.sleep(0.5)

for x in arr_pin:
  GPIO.output(x, False)


