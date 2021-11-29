#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

from example1 import FRESH

LED = 18
FRESH = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.HIGH)
try: 
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(FRESH)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(FRESH)
except KeyboardInterrupt:
    GPIO.cleanup()
