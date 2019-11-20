####################### Library definitions ###################################
import serial
from time import sleep
import matplotlib.pyplot as plt
from drawnow import *
import numpy as np
from scipy import signal
from math import pi
from decimal import Decimal
import scipy.fftpack

###################### Variable declarations ##################################
Res = []
ResAvg = np.asarray([])
plt.ion() # Interactive mode to plot live data
column = 0
row = 0
i = 0
x = np.linspace(0,14,15)

COM = 'COM4'# /dev/ttyACM0 (Linux)
BAUD = 4800

ser = serial.Serial(COM, BAUD, timeout = 0.1)

state = 0

inputvar = '0'

Window = 0
Iterations = 0
Order = 4
###################### Function definitions ###################################
def makeFig():
	plt.ylim(-1,1) #Set y min and max values
	plt.title('Serial plotter') #Plot the title
	plt.grid(True) #Turn the grid on
	plt.ylabel('Decoded value') #Set ylabels
	plt.plot(xf,   ResAvg, 'ro-', label='Received value') #plot the received value
	plt.legend(loc='upper left') #plot the legend
	plt.show(block = False)

def filterDesign():
    f = []
    g = []
    f_s = 48000
    bands = 3
    
    for i in range(bands):
        temp = float(input("Input edge "))
        omega_c_d = temp * 2/ f_s    # Normalized cut-off frequency (digital)
        f.append(omega_c_d)
    for i in range(bands):
        temp2 = float(input("Input gain "))
        g.append(temp2)
        
    
    b = signal.firwin2(Order, [((0)*2/f_s),(f[0]),(f[1]),(f[2]),((24000*2)/f_s)],[0,g[0],g[1],g[2],0])
    print("Coefficients")
    print("b = ",b)
    return b

###################### Program flow ###########################################
print('Waiting for device');
sleep(3)
print(ser.name)
print(BAUD)

while state >= 0:
    if state == 0:
        print('-------------Main Menu-------------')
        print('Press the number of the option wanted')
        print('1. Desgin filter')
        print('2. Receive data')
        print('3. Help')
        print('4. Quit')
        
        state = int(input())
        
    elif state == 5:
        inputvar = str(coeff)
        x = inputvar.replace(" ","")
        y = x.replace("[","")
        z = y.replace("]","")
        s = z.replace("'","")
        q = s + 'p';
        ser.write(z.encode())
        ser = None # Closes port   
        print('Returning to Main Menu...')
        state = 0
        
    elif state == 2:
        print("Input window size")
        Iterations = int(input())
        Window = 1
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
                
            ResAvg = scipy.fftpack.fft(ResNumL)
            xf = np.linspace(0.0, 48000/(2.0), 1024/2)
            
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
    
    elif state == 1:
        coeff = list(filterDesign())
        for i in range(Order):
            coeff[i] = np.format_float_positional(coeff[i])
        state = 5;
    
    elif state == 4:
        state = -1
        ser = None # Closes port
    
    else:
        print('Command not recognized')
        print('Returning to Main Menu...')
