import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


while True:
  GPIO.output(3, True)
  GPIO.output(5, True)
  GPIO.output(7, True)
  GPIO.output(8, True)
  GPIO.output(10, True)
  GPIO.output(11, True)
  GPIO.output(12, True)
  GPIO.output(13, True)
  GPIO.output(15, True)
  GPIO.output(16, True)
  GPIO.output(18, True)
  GPIO.output(19, True)
  GPIO.output(21, True)
  GPIO.output(22, True)
  GPIO.output(23, True)
  GPIO.output(24, True)

  time.sleep(1)

  GPIO.output(3, False)
  GPIO.output(5, False)
  GPIO.output(7, False)
  GPIO.output(8, False)
  GPIO.output(10, False)
  GPIO.output(11, False)
  GPIO.output(12, False)
  GPIO.output(13, False)
  GPIO.output(15, False)
  GPIO.output(16, False)
  GPIO.output(18, False)
  GPIO.output(19, False)
  GPIO.output(21, False)
  GPIO.output(22, False)
  GPIO.output(23, False)
  GPIO.output(24, False)

  time.sleep(1)