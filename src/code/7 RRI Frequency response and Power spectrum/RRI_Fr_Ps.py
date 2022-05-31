# from pprint import pprint
from matplotlib import pyplot as plt
from scipy.fftpack import fft, fftfreq
from RR_Class import RRClass
import numpy as np

# import scipy.fftpack

# open the folder
rrDataCenter = RRClass()
RRDataBase = rrDataCenter.get_data_base()
taNames = rrDataCenter.get_ta_name()

# Check is it ok
# pprint(RRDataBase['CW']['baseline'])

testData = RRDataBase["CW"]["baseline"]
N = testData.size
T = 1.0 / 25000.0
x = np.linspace(0.0, N * T, N)
y = testData.values
yf = np.abs(fft(y))
xf = fftfreq(testData.size, d=T)

fig, ax = plt.subplots()
ax.plot(np.abs(xf), np.abs(yf))
plt.show()
