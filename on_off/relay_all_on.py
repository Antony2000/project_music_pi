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

GPIO.output(3, False)
GPIO.output(5, False)
GPIO.output(7, False)
GPIO.output(8, False)
GPIO.output(26, False)
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
