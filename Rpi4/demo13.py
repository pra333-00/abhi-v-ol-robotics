from time import sleep
from smbus import SMBus
bus = SMBus(1)
bus.write_byte(0X48,2)

while True:
	read = bus.read_byte(0X48)
	print(read)
	sleep(1)
