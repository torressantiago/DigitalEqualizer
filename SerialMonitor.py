import serial
from time import sleep
import sys


COM = 'COM3'# /dev/ttyACM0 (Linux)
BAUD = 128000

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(3)
print(ser.name)

#check args
monitor = True


while True:
	val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
	valA = val.split("/")
	#print()
	if(monitor == True):
		print(val, end="\r\n", flush=True)
