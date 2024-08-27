#!/usr/bin/python
# encoding:utf-8
import RPi.GPIO as GPIO
import time
pin_rain=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_rain, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
	while True:
		status = GPIO.input(pin_rain)
		if status == True:
			print(' Im raindrop module , No raindrops were detected , Everything is all right ！')
		else:
			print(' Im raindrop module , Raindrops detected , Activate monitoring ')
			time.sleep(0.5)
except KeyboradInterrupt:
	GPIO.cleanup()
