import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
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
  time.sleep(0.1)
  GPIO.output(5, True)
  time.sleep(0.1)
  GPIO.output(7, True)
  time.sleep(0.1)
  GPIO.output(8, True)
  time.sleep(0.1)
  GPIO.output(26, True)
  time.sleep(0.1)
  GPIO.output(11, True)
  time.sleep(0.1)
  GPIO.output(12, True)
  time.sleep(0.1)
  GPIO.output(13, True)
  time.sleep(0.1)
  GPIO.output(15, True)
  time.sleep(0.1)
  GPIO.output(16, True)
  time.sleep(0.1)
  GPIO.output(18, True)
  time.sleep(0.1)
  GPIO.output(19, True)
  time.sleep(0.1)
  GPIO.output(21, True)
  time.sleep(0.1)
  GPIO.output(22, True)
  time.sleep(0.1)
  GPIO.output(23, True)
  time.sleep(0.1)
  GPIO.output(24, True)
  time.sleep(0.1)

  GPIO.output(3, False)
  time.sleep(0.1)
  GPIO.output(5, False)
  time.sleep(0.1)
  GPIO.output(7, False)
  time.sleep(0.1)
  GPIO.output(8, False)
  time.sleep(0.1)
  GPIO.output(26, False)
  time.sleep(0.1)
  GPIO.output(11, False)
  time.sleep(0.1)
  GPIO.output(12, False)
  time.sleep(0.1)
  GPIO.output(13, False)
  time.sleep(0.1)
  GPIO.output(15, False)
  time.sleep(0.1)
  GPIO.output(16, False)
  time.sleep(0.1)
  GPIO.output(18, False)
  time.sleep(0.1)
  GPIO.output(19, False)
  time.sleep(0.1)
  GPIO.output(21, False)
  time.sleep(0.1)
  GPIO.output(22, False)
  time.sleep(0.1)
  GPIO.output(23, False)
  time.sleep(0.1)
  GPIO.output(24, False)
  time.sleep(0.1)