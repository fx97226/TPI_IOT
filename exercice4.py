#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
LED = 2
LED2 = 3
LED3 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED, GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED2, GPIO.LOW)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED3, GPIO.LOW)
states = [False, False, False]
DELAY = 0.5
try:
    while True:
            button_state=GPIO.input(17)
            button_state1=GPIO.input(27)
            button_state2=GPIO.input(22)
            if button_state == True:
                if (states[0] == True) 
                    GPIO.output(LED, GPIO.HIGH)
                    states[0] = True
                else:
                    GPIO.output(LED, GPIO.LOW)
                    states[0] = False
            if button_state == True:
                if (states[1] == True)
                    GPIO.output(LED, GPIO.HIGH)
                    states[1] = True
                else:
                    GPIO.output(LED, GPIO.LOW)
                    states[1] = False
            if button_state == True:
                if (states[2] == True)
                    GPIO.output(LED, GPIO.HIGH)
                    states[2] = True
                else:
                    GPIO.output(LED, GPIO.LOW)
                    states[2] = False
            time.sleep(DELAY)
except KeyboardInterrupt:
    GPIO.cleanup()
