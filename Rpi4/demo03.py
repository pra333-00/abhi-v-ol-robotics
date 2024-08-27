import RPi.GPIO as a
import time
a.setmode(a.BOARD)
a.setup(10,a.OUT)
a.setup(12,a.OUT)
a.setup(16,a.OUT)
while (True):
	a.output(10,True)
	time.sleep(1)
	a.output(10,False)
	a.output(12,True)
	time.sleep(1)
	a.output(12,False)
	a.output(16,True)
	time.sleep(1)
	a.output(16,False)
