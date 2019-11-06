# Digital filter design
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Butterworth lowpass, fs = 48000, order 4
a,b = signal.iirfilter(4, [200], btype='lp',
                       analog=False, ftype='butter', fs=48000,
                       output='ba')
w, h = signal.sosfreqz(sos, 2000, fs=2000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((0, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()
