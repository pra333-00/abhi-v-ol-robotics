import RPi.GPIO as a
import time
import serial as s
a.setmode(a.BOARD)
a.setup(12,a.OUT)
ser=s.Serial(port="/dev/ttyS0",baudrate=9600)

while True:
	a.output(12,True)
	ser.write("\nON")
	time.sleep(1)
