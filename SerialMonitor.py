####################### Library definitions ###################################
import serial
from time import sleep
import matplotlib.pyplot as plt
from drawnow import *
import numpy as np

###################### Variable declarations ##################################
Res = []
ResNumL = np.ones((15,3))
ResAvg = np.asarray([])
plt.ion() # Interactive mode to plot live data
column = 0
row = 0
i = 0
x = np.linspace(0,14,15)

COM = 'COM10'# /dev/ttyACM0 (Linux)
BAUD = 2400

ser = serial.Serial(COM, BAUD, timeout = 0.1)

###################### Function definitions ###################################
def makeFig():
	plt.ylim(-1,1) #Set y min and max values
	plt.title('Serial plotter') #Plot the title
	plt.grid(True) #Turn the grid on
	plt.ylabel('Decoded value') #Set ylabels
	plt.plot(ResAvg, 'ro-', label='Received value') #plot the received value
	plt.legend(loc='upper left') #plot the legend
	plt.show(block = True)


###################### Program flow ###########################################
print('Waiting for device');
sleep(3)
print(ser.name)

for BigCounter in range(3):
    print(BigCounter)
    column = int(BigCounter)
    for counter in x:
        print(counter)
        row = int(counter)
        ResString = str(ser.readline().decode().strip('\r\n')) # Capture serial output as a decoded string
        ResNum = float(ResString)
        Res.append(ResNum)
        ResNumL[row][column] = np.asarray(ResNum)
        
    ResAvg = np.mean(ResNumL,axis = 1)
    
drawnow(makeFig) # plot average after window
        
ser = None # Closes port
