import RPi.GPIO as a
import time
a.setmode(a.BOARD)
a.setup(8,a.OUT)
a.output(8,True)
while (True):
    a.output(8,False)
    time.sleep(1)
    a.output(8,True)
    time.sleep(1)
