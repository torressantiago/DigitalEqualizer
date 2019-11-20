from scipy import signal
import numpy as np
from math import pi

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
    

b = signal.firwin2(60, [((0)*2/f_s),(f[0]),(f[1]),(f[2]),((24000*2)/f_s)],[0,g[0],g[1],g[2],0])
print("Coefficients")
print("b = ",b)



w, h = signal.freqz(b)
w *= f_s / (2 * pi)                       # Convert from rad/sample to Hz

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [Hz]')
ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid()
ax2.axis('tight')
plt.show()
