#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LEDR = 11
LEDG = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDR,GPIO.OUT)
GPIO.setup(LEDG,GPIO.OUT)

try:
	while True:	
		GPIO.output(LEDR,GPIO.HIGH)
		GPIO.output(LEDG,GPIO.HIGH)

except KeyboardInterrupt: 
	GPIO.output(LEDR,GPIO.LOW)
	GPIO.output(LEDG,GPIO.LOW)
	GPIO.cleanup()
