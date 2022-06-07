from matplotlib import pyplot as plt
import numpy as np
from scipy.fftpack import fft, fftfreq
from RR_Class import RRClass

# open the folder
rrDataCenter = RRClass()
rrDataBase = rrDataCenter.get_data_base_M2()
taNames = rrDataCenter.get_ta_name()
typeFiles = rrDataCenter.get_state_menu()

# Number of sample points

testData = rrDataBase['CW']['baseline']
data = list(testData)
N = testData.size

# Sample spacing
T = 1.0 / 800.0  # f = 60 Hz

# Create a signal
x = np.linspace(0.0, N * T, N)
# t0 = np.pi / 6  # non-zero phase of the second sine
y = data  # np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(200.0 * 2.0 * np.pi * x + t0)
yf = fft(y)  # to normalize use norm='ortho' as an additional argument

# Where is a 200 Hz frequency in the results?
freq = fftfreq(x.size, d=T)
index, = np.where(np.isclose(freq, 200, atol=1 / (T * N)))

# Get magnitude and phase
magnitude = np.abs(yf[index[0]])
phase = np.angle(yf[index[0]])
print("Magnitude:", magnitude, ", phase:", phase)

# Plot a spectrum
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(freq[0:N // 2], 2 / N * np.abs(yf[0:N // 2]))
ax1.set_title('amplitude spectrum')

ax2.plot(freq[0:N // 2], np.angle(yf[0:N // 2]))
ax2.set_title('phase spectrum')
plt.show()
'''
plt.plot(freq[0:N // 2],
         2 / N * np.abs(yf[0:N // 2]),
         label='amplitude spectrum')  # in a conventional form
plt.plot(freq[0:N // 2], np.angle(yf[0:N // 2]), label='phase spectrum')
plt.legend()
plt.grid()
plt.show()
'''
