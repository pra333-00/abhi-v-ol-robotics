import RPi.GPIO as a
import time
a.setmode(a.BOARD)
a.setup(10,a.OUT)
a.setup(12,a.IN)
a.output(10,True)

while (True):
	iVal = a.input(12)
	if(iVal==True):
		a.output(10,False)
		time.sleep(1)
		a.output(10,True)
		time.sleep(1)
	else:
		a.output(10,False)

