import RPi.GPIO as a
import time
a.setmode(a.BOARD)
a.setup(12,a.OUT)
a.setwarnings(False)
t=a.PWM(12,50)

while True:
	for i in range(0,100,5):
		t.start(i)
		time.sleep(1)
		t.start(100-i)
		time.sleep(1)
