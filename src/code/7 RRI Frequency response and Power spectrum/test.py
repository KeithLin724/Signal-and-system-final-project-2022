from matplotlib import pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
from RR_Class import RRClass

# open the folder
rrDataCenter = RRClass()
rrDataBase = rrDataCenter.get_data_base_M2()
taNames = rrDataCenter.get_ta_name()
typeFiles = rrDataCenter.get_state_menu()
# print(typeFiles)

# Check is it ok
# pprint(RRDataBase['CW']['baseline'])

testData = rrDataBase['CW']['baseline']
data = list(testData)

N = testData.size
T = 1.0 / 25000.0
np.disp('DFT of the sequence x(n)')
Xk = fft(data, N)

np.disp('The Mag sequence x(n)')
MagXk = np.abs(Xk)

np.disp('The Phase sequence')
PhaXk = np.angle(Xk)

np.disp('Inverse DFT of the sequence Xk')
Xn = ifft(Xk)

n = np.linspace(0.0, N * T, N)
wk = np.linspace(0.0, N * T, N)

fig, ax = plt.subplots()
# ax.plot(np.abs(xf), np.abs(yf))
# ax.plot(np.abs(xLog), np.abs(yLog))
ax.plot(n, MagXk)
plt.show()
