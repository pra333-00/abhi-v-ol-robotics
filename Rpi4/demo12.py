import RPi.GPIO as a
import time
import serial as s
ser=s.Serial(port="/dev/ttyS0",baudrate=9600)
a.setmode(a.BOARD)
a.setup(12,a.OUT)
a.output(12,True)

while True:
	                                                                                                                                                                           decision=raw_input("\nenter on or off in lowercase only")
	if(decision=="on"):
		ser.write("\nON")
		a.output(12,True)
	elif(decision=="off"):
		ser.write("\nOFF")
		a.output(12,False)
	else:
		print("\nenter your input properly")
		ser.write("\nenter your input properly")  
