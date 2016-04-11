#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LEDR = 11
LEDG = 12

TIME = 0.1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDR,GPIO.OUT)
GPIO.setup(LEDG,GPIO.OUT)

pwmG = GPIO.PWM(LEDG, 2000)
pwmR = GPIO.PWM(LEDR, 2000)

try:
	pwmG.start(0)
	pwmR.start(0)
	while True:
		for dc in range(0,101,5):
			pwmG.ChangeDutyCycle(dc)
			for dc2 in range(0,101,5):
				print 'G: %d, R: %d' % (dc,dc2)
				pwmR.ChangeDutyCycle(dc2)
				time.sleep(TIME)


                for dc in range(100,-1,-5):
                        pwmR.ChangeDutyCycle(dc)
                        for dc2 in range(100,-1,-5):
                                print 'G: %d, R: %d' % (dc2,dc)
                                pwmG.ChangeDutyCycle(dc2)
                                time.sleep(TIME)
							
except KeyboardInterrupt: 
	pwmG.stop()
	pwmR.stop()
	GPIO.cleanup()
	
