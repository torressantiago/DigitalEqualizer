####################### Library definitions ###################################
import serial
from time import sleep
import matplotlib.pyplot as plt
from drawnow import *
import numpy as np

###################### Variable declarations ##################################
Res = []
ResAvg = np.asarray([])
plt.ion() # Interactive mode to plot live data
column = 0
row = 0
i = 0
x = np.linspace(0,14,15)

COM = 'COM10'# /dev/ttyACM0 (Linux)
BAUD = 2400

ser = serial.Serial(COM, BAUD, timeout = 0.1)

state = 0

inputvar = '0'

Window = 0
Iterations = 0
###################### Function definitions ###################################
def makeFig():
	plt.ylim(-1,1) #Set y min and max values
	plt.title('Serial plotter') #Plot the title
	plt.grid(True) #Turn the grid on
	plt.ylabel('Decoded value') #Set ylabels
	plt.plot(ResAvg, 'ro-', label='Received value') #plot the received value
	plt.legend(loc='upper left') #plot the legend
	plt.show(block = False)


###################### Program flow ###########################################
print('Waiting for device');
sleep(3)
print(ser.name)
print(BAUD)

while state >= 0:
    if state == 0:
        print('-------------Main Menu-------------')
        print('Press the number of the option wanted')
        print('1. Send data')
        print('2. Receive data')
        print('3. Help')
        print('4. Quit')
        
        state = int(input())
        
    elif state == 1:
        print("Input the value you want to send")
        inputvar = input()
        inputvar += "\r\n"
        ser.write(inputvar.encode())
            
        ser = None # Closes port   
        print('Returning to Main Menu...')
        state = 0
        
    elif state == 2:
        print("Input number of iterations and window size")
        Iterations = int(input())
        Window = int(input())
        ResNumL = np.ones((Window,Iterations))
        for BigCounter in range(Iterations):
            print(BigCounter)
            column = int(BigCounter)
            for counter in range(Window):
                print(counter)
                row = int(counter)
                ResString = str(ser.readline().decode().strip('\r\n')) # Capture serial output as a decoded string
                ResNum = float(ResString)
                print(ResNum)
                Res.append(ResNum)
                ResNumL[row][column] = np.asarray(ResNum)
                
            ResAvg = np.mean(ResNumL,axis = 1)
            
        drawnow(makeFig) # plot average after window
                
        ser = None # Closes port
        print('Returning to Main Menu...')
        state = 0
        
    elif state == 3:
        print('-------------Help-------------')
        print('This program can receive/send at a certain baudrate information received using serial protocol')
        print('To change baudrate and port, please change BAUD and COM respectively in code')
        print('Returning to Main Menu...')
        state = 0
    
    elif state == 4:
        state = -1
        ser = None # Closes port
    
    else:
        print('Command not recognized')
        print('Returning to Main Menu...')
