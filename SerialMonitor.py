import serial
from time import sleep
import matplotlib.pyplot as plt
from drawnow import *
import numpy as np

Res = []
ResNumL = [[]]
plt.ion() # Interactive mode to plot live data
i = 0
x = np.linspace(1,15,15)

def makeFig():
	plt.ylim(-1,1) #Set y min and max values
	plt.title('Serial plotter') #Plot the title
	plt.grid(True) #Turn the grid on
	plt.ylabel('Decoded value') #Set ylabels
	plt.plot(Res, 'ro', label='Received value') #plot the temperature
	plt.legend(loc='upper left') #plot the legend
	plt.draw()



COM = 'COM10'# /dev/ttyACM0 (Linux)
BAUD = 2000000

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(3)
print(ser.name)

for BigCounter in range(3):
    for counter in x:
        ResString = str(ser.readline().decode().strip('\r'))#Capture serial output as a decoded string
        ResNum = float(ResString)
        print(ResString)
        Res.append(ResNum)
        drawnow(makeFig)
    #	i = i + 1
    #	if(i > 15):                          
    #		Res.pop(0) # This allows to just see the last 15 data points
#    plt.ylim(-1,1) #Set y min and max values
#    plt.title('Serial plotter') #Plot the title
#    plt.grid(True) #Turn the grid on
#    plt.ylabel('Decoded value') #Set ylabels
#    plt.plot(x,Res, label='Received value') #plot the temperature
#    plt.legend(loc='upper left') #plot the legend
#    plt.draw()
