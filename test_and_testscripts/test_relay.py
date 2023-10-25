import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)


while True:
  GPIO.output(3, True)
  GPIO.output(5, True)
  GPIO.output(7, True)
  GPIO.output(8, True)
  GPIO.output(10, True)
  GPIO.output(12, True)
  time.sleep(1)
  GPIO.output(3, False)
  GPIO.output(5, False)
  GPIO.output(7, False)
  GPIO.output(8, False)
  GPIO.output(10, False)
  GPIO.output(12, False)
  time.sleep(1)