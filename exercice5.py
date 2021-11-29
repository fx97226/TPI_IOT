#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
GREEN = 2
YEL = 3
RED = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(GREEN, GPIO.LOW)
GPIO.setup(YEL, GPIO.OUT)
GPIO.setup(YEL, GPIO.LOW)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(RED, GPIO.LOW)
DELAY = 0.5
try:
    while True:
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(YEL, GPIO.HIGH)
        GPIO.output(YEL, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(DELAY)
except KeyboardInterrupt:
    GPIO.cleanup()
