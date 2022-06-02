# from pprint import pprint
from matplotlib import pyplot as plt
from scipy.fftpack import fft, fftfreq
from RR_Class import RRClass
import numpy as np
# import control.matlab as ml
# from rich import print

# import scipy.fftpack

# open the folder
rrDataCenter = RRClass()
rrDataBase = rrDataCenter.get_data_base()
rrDataBaseM2 = rrDataCenter.get_data_base_M2()
taNames = rrDataCenter.get_ta_name()
typeFiles = rrDataCenter.get_state_menu()
# print(typeFiles)

# Check is it ok
# pprint(RRDataBase['CW']['baseline'])

# testData = rrDataBase['CW']['baseline']
testData = rrDataBaseM2['CW']['baseline']
N = testData.size
T = 1.0 / 25000.0
x = np.linspace(0.0, N * T, N)  # np.linspace(0.0, N * T, N)
y = testData.values
yFFT = fft(y)
yf = np.abs(yFFT)
yPhase = np.angle(yFFT)
amp = 2 / N * yf
xf = fftfreq(testData.size, d=T)
# yLog = [np.log10(i) for i in yf]
# xLog = [np.log10(i) for i in xf]

# print(yLog)

fig, ax = plt.subplots()
# ax.plot(np.abs(xf), np.abs(yf))
# ax.plot(np.abs(xLog), np.abs(yLog))
ax.plot(np.abs(xf), np.abs(yPhase))
plt.show()
