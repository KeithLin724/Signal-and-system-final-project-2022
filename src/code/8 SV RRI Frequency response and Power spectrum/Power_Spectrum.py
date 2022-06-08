from cmath import log10
import numpy as np
from numpy.fft import fft

# test
# from RR_Class import RRClass
# test


class PowerSpectrum:

    def __init__(self, dataIn) -> None:
        self.__data = dataIn
        self.__N = self.__data.size
        self.__fr = np.linspace(0, 800.0 // 2, self.__N // 2)
        self.__fftData = fft(self.__data)
        xFTmp = self.__fftData[0:self.__N // 2]
        self.__powerSpectrum = abs(xFTmp)**2

    def total_power(self):

        return 10 * log10(sum(list(self.__powerSpectrum)))


# test
# rrDataCenter = RRClass()
# rrDataBase = rrDataCenter.get_data_base_M2()
# testData = rrDataBase['CW']['baseline']
# data = list(testData)

# print(data)
# power = PowerSpectrum(testData)
# print(power.total_power())