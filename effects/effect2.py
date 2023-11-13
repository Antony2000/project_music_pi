import RPi.GPIO as GPIO
import time
from itertools import chain

arr_pin1 = [3,5,7,8]
arr_pin2 = [26,11,12,13]
arr_pin3 = [15,16,18,19]
arr_pin4 = [21,22,23,24]
all_arr = [3,5,7,8,26,11,12,13,15,16,18,19,21,22,23,24]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

for x in all_arr:
  GPIO.setup(x, GPIO.OUT)

for x in all_arr:
    GPIO.output(x, True)
time.sleep(0.5)

for i in range(5):
    for x in arr_pin1:
      GPIO.output(x, False)
    time.sleep(0.5)
    for x in arr_pin1:
      GPIO.output(x, True)
    time.sleep(0.5)
    for x in arr_pin2:
      GPIO.output(x, False)
    time.sleep(0.5)
    for x in arr_pin2:
      GPIO.output(x, True)
    time.sleep(0.5)
    for x in arr_pin3:
      GPIO.output(x, False)
    time.sleep(0.5)
    for x in arr_pin3:
      GPIO.output(x, True)
    time.sleep(0.5)
    for x in arr_pin4:
      GPIO.output(x, False)
    time.sleep(0.5)
    for x in arr_pin4:
      GPIO.output(x, True)
    time.sleep(0.5)

for x in all_arr:
    GPIO.output(x, False)

