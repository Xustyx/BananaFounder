#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LEDR = 11
LEDG = 12

TIME = 0.025

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDR,GPIO.OUT)
GPIO.setup(LEDG,GPIO.OUT)

pwmG = GPIO.PWM(LEDG, 2000)
pwmR = GPIO.PWM(LEDR, 2000)

def map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):   # For example : col = 0x112233
        R_val = (col & 0x00FF)
	G_val = ((col & 0xFF00) >> 8)
	print '(Hex) => G: %x, R: %x' % (G_val,R_val)

        R_val = map(R_val, 0, 255, 0, 100)
        G_val = map(G_val, 0, 255, 0, 100)

        pwmR.ChangeDutyCycle(R_val)     # Change duty cycle
        pwmG.ChangeDutyCycle(G_val)
	print '(Prc) => G: %d, R: %d' % (G_val,R_val)

try:
	pwmG.start(0)
	pwmR.start(0)
	while True:
		for dc in range(0x00,0x10000,0x01):
			print '(Hex) => current: %x' % dc
			setColor(dc)
			time.sleep(TIME)

except KeyboardInterrupt: 
	pwmG.stop()
	pwmR.stop()
	GPIO.cleanup()
	
