import RPi.GPIO as GPIO
from time import sleep

LED_PIN=40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

while True:
	GPIO.output(LED_PIN, GPIO.HIGH)
	sleep(1)
	GPIO.output(LED_PIN, GPIO.LOW)
	sleep(1)


