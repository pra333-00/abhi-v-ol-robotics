import RPi.GPIO as a
import time
import serial as s
ser=s.Serial(port="/dev/ttyS0",baudrate=9600)

while True:
	ser.write("Abhinav Vattimilli")
	time.sleep(1)
