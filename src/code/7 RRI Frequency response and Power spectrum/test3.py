import ctypes
from matplotlib import pyplot as plt
import numpy as np
from numpy.fft import fft  # , fftfreq
from RR_Class import RRClass


def get_ppi():
    '''get the dpi function'''
    LOGPIXELSX, user32 = (88, ctypes.windll.user32)

    user32.SetProcessDPIAware()
    dc = user32.GetDC(0)
    pix_per_inch = ctypes.windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
    user32.ReleaseDC(0, dc)
    return pix_per_inch


Dpi = get_ppi()

# open the folder
rrDataCenter = RRClass()
rrDataBase = rrDataCenter.get_data_base_M2()
taNames = rrDataCenter.get_ta_name()
typeFiles = rrDataCenter.get_state_menu()

# Number of sample points

testData = rrDataBase['CW']['baseline']
data = list(testData)
N, T = testData.size, 1.0 / 800.0  # f = 60 Hz

# Create a signal
x, y = np.linspace(0.0, N * T, N), data
yf = fft(y)  # to normalize use norm='ortho' as an additional argument
print('length of yf = ', len(yf))

# Where is a 200 Hz frequency in the results?
freq = np.linspace(0.0, 0.5, N // 2)  # fftfreq(x.size, d=T)
# index, = np.where(np.isclose(freq, 200, atol=1 / (T * N)))
# print(f'length of frequency[N/2] = {len(freq[0:N // 2])}')
# Get magnitude and phase
# magnitude = np.abs(yf[index[0]])
# phase = np.angle(yf[index[0]])
# print("Magnitude:", magnitude, ", phase:", phase)

# Plot a spectrum
plt.figure(figsize=(16, 12))

# fig, ax2D = plt.subplots(2, 2)
plt.subplot(2, 2, 1)
plt.plot(x, testData)
plt.title('RRI spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('RRI values')
plt.grid()

# Amplitude spectrum
# mag
xMag = np.abs(yf[0:N // 2]) / N
xMagPlot = 2 * xMag[0:int(N / 2 + 1)]
xMagPlot[0] = xMagPlot[0] / 2
plt.subplot(2, 2, 2)
plt.semilogy(freq, xMagPlot)
# plt.semilogy(freq[0:N // 2], 2 / N * np.abs(yf[0:N // 2]))
plt.title('Amplitude spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (s)')
plt.grid()

# Phase spectrum
plt.subplot(2, 2, 3)
plt.plot(freq, np.angle(yf[0:N // 2]))
# plt.semilogy(freq[0:N // 2], np.angle(yf[0:N // 2]))
plt.title('Phase spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phrase (rad)')
plt.grid()

# Power spectrum
plt.subplot(2, 2, 4)
xF = yf[0:N // 2]
fr = np.linspace(0, 800 // 2, N // 2)
plt.semilogy(fr, abs(xF)**2)
plt.title('Power spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PS D(s^2/Hz)')
plt.grid()
# plt.psd()

plt.savefig('src\\code\\7 RRI Frequency response and Power spectrum\\test.png',
            dpi=Dpi)
plt.show()
print(freq)
'''
plt.plot(freq[0:N // 2],
         2 / N * np.abs(yf[0:N // 2]),
         label='amplitude spectrum')  # in a conventional form
plt.plot(freq[0:N // 2], np.angle(yf[0:N // 2]), label='phase spectrum')
plt.legend()
plt.grid()
plt.show()
'''
