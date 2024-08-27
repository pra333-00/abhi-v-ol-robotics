import RPi.GPIO as a
import time
a.setmode(a.BOARD)
a.setup(10, a.OUT)
while True:
	on_off=raw_input('Enter on/off: ').lower()
	if on_off == 'on':
		a.output(10, True)
	elif on_off == 'off':
		a.output(10, False)
