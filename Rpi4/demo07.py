import RPi.GPIO as a
import time
a.setmode(a.BOARD)
a.setup(12,a.OUT)
a.setup(10,a.OUT)
a.setwarnings(False)
t=a.PWM(12,50)
q=a.PWM(10,50)

while True:
	for i in range(0,100,5):
		t.start(i)
		time.sleep(1)
	for i in range(100,0,-5):
		q.start(i)
		time.sleep(1)
