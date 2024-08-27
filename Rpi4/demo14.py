import RPi.GPIO as a
import time
import serial as s
ser=s.Serial(port="/dev/ttyS0",baudrate=9600)
a.setmode(a.BOARD)
a.setup(12,a.OUT)
a.output(12,True)

while True:
	x=ser.readline()
	x=x.strip()
	print(x)
	print(len(x))
	if(x.upper()=="ON"):
		a.output(12,True)
	elif(x.upper()=="OFF"):
		a.output(12,False)

