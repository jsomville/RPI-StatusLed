#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

LED_PIN=40
BLINK_DELAY=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    sleep(BLINK_DELAY)
    GPIO.output(LED_PIN, GPIO.LOW)
    sleep(BLINK_DELAY)
