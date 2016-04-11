#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LED = 15
WAIT = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

try:
	while True:
		print 'Led on!'
		GPIO.output(LED, GPIO.HIGH)
		time.sleep(WAIT)

		print 'Led off!'
		GPIO.output(LED, GPIO.LOW)
		time.sleep(WAIT)

except KeyboardInterrupt:
	GPIO.output(LED, GPIO.LOW)
	GPIO.cleanup()
