import os
from matplotlib import pyplot as plt
import pandas as pd
from rich import print
import numpy as np
from numpy.fft import fft, fftfreq


def fft_and_phase(dataList: pd.Series, savePath: str) -> None:
    data = list(dataList)
    N, T = dataList.size, 1.0 / 800.0

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
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.plot(freq[0:N // 2], 2 / N * np.abs(yf[0:N // 2]))
    ax1.set_title('amplitude spectrum')

    ax2.plot(freq[0:N // 2], np.angle(yf[0:N // 2]))
    ax2.set_title('phase spectrum')

    xF = yf[0:N // 2]
    fr = np.linspace(0, 800 // 2, N // 2)
    ax3.plot(fr, abs(xF)**2)
    ax3.set_title('Power spectrum')
    # plt.psd()
    plt.show()


class RRClass:
    """_summary_
    
        This a class of RR classes
        read the folder about the RR data (.csv file) 
    """

    def __init__(self) -> None:

        self.__mainFolderName, self.__folderName, self.__folderNameM2 = 'src', 'RR_csv', 'RRM2_csv'
        self.__taName = ('CW', 'HT')
        self.__dataBaseType = ('RR', 'RRM2')
        self.__fileState = []
        self.__dataBase, self.__dataBaseM2, self.__dataBaseAll = (dict(),
                                                                  dict(),
                                                                  dict())

        tmpTaDataAll = [[], []]

        findPathAllList = (os.path.join(self.__mainFolderName,
                                        self.__folderName),
                           os.path.join(self.__mainFolderName,
                                        self.__folderNameM2))

        # TODO: this path is it exists
        for findPath in findPathAllList:
            if not os.path.exists(findPath) and not os.path.isdir(findPath):
                print(f"path is not found\nPath : {findPath}")
                exit()

        for taName in self.__taName:

            tmpPathList = [
                os.path.join(filePath, taName) for filePath in findPathAllList
            ]

            # check the path is it exists
            for tmpPathObj in tmpPathList:
                if not os.path.exists(tmpPathObj):
                    print(f"path is not found\nPath : {tmpPathObj}")
                    exit()

            # TODO: Read the under folder file
            listOfFileNameAllList = [os.listdir(i) for i in tmpPathList]
            replaceName = ['RR_', 'RRM2_']

            usingFor = list(
                zip(listOfFileNameAllList, tmpTaDataAll, tmpPathList,
                    replaceName))

            for listOfFileName, tmpTaData, tmpPath, takeName in usingFor:
                tmpTaDict = dict()
                for objFile in listOfFileName:
                    dataRead = pd.read_csv(os.path.join(tmpPath, objFile),
                                           index_col=False,
                                           header=0).squeeze("columns")
                    # get header data
                    tmpHeader = [float(dataRead.name)]
                    tmpHeader[1:] = dataRead
                    dataRead = pd.Series(tmpHeader)

                    # get state
                    fileState = objFile.replace('.csv',
                                                '').replace(takeName, '')
                    self.__fileState.append(fileState)
                    tmpTaDict.update({fileState: dataRead})

                tmpTaData.append(tmpTaDict)

        # base data
        self.__dataBase = dict(zip(self.__taName, tmpTaDataAll[0]))
        self.__dataBaseM2 = dict(zip(self.__taName, tmpTaDataAll[1]))

        # add data
        self.__dataBaseAll = dict(
            zip(self.__dataBaseType, [self.__dataBase, self.__dataBaseM2]))

        self.__fileState = tuple(set(self.__fileState))

    def get_data_base(self) -> dict:
        """get the data base of RR_csv(Name --> State --> Data)"""
        return self.__dataBase

    def get_data_base_M2(self) -> dict:
        """get the data base of RRM2_csv(Name --> State --> Data) M2"""
        return self.__dataBaseM2

    def get_ta_name(self) -> tuple:
        """get ta name"""
        return self.__taName

    def get_state_menu(self) -> tuple:
        """get file state list"""
        return self.__fileState

    def get_data_base_type(self) -> tuple:
        '''get the data base type (RR or RRM2)'''
        return self.__dataBaseType

    def get_data_base_all(self) -> dict():
        '''get the data base (Data Base type--> Name --> State --> Data)'''
        return self.__dataBaseAll


# debug
'''
tmp = RRClass()
cw = tmp.get_data_base()['CW']
ht = tmp.get_data_base()['HT']
all_data = tmp.get_data_base_all()
print(all_data)
'''
