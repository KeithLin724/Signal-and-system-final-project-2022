import os
import pandas as pd
from rich import print
import numpy as np


def fft_and_phase(dataList: pd.Series, savePath: str) -> None:
    N, T = dataList.size, 1.0 / 25000.0
    x, y = np.linspace(0.0, N * T, N), dataList.values


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
        tmpTaData, tmpTaDataM2 = [], []

        findPath, findPathM2 = (os.path.join(self.__mainFolderName,
                                             self.__folderName),
                                os.path.join(self.__mainFolderName,
                                             self.__folderNameM2))

        # TODO: this path is it exists
        if not os.path.exists(findPath) and not os.path.isdir(findPath):
            print(f"path is not found\nPath : {tmpPath}")
            exit()
        # TODO: add the new path
        if not os.path.exists(findPathM2) and not os.path.isdir(findPathM2):
            print(f"path is not found\nPath : {tmpPath}")
            exit()

        for taName in self.__taName:
            tmpPath, tmpPathM2 = (os.path.join(findPath, taName),
                                  os.path.join(findPathM2, taName))

            if not os.path.exists(tmpPath):
                print(f"path is not found\nPath : {tmpPath}")
                exit()

            if not os.path.exists(tmpPathM2):
                print(f"path is not found\nPath : {tmpPath}")
                exit()

            # TODO: Read the under folder file
            listOfFileName, listOfFileNameM2 = (os.listdir(tmpPath),
                                                os.listdir(tmpPathM2))
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
                fileState = objFile.replace('.csv', '').replace('RR_', '')
                self.__fileState.append(fileState)
                tmpTaDict.update({fileState: dataRead})

            tmpTaData.append(tmpTaDict)

            tmpTaDict = dict()

            for objFile in listOfFileNameM2:
                dataRead = pd.read_csv(os.path.join(tmpPathM2, objFile),
                                       index_col=False,
                                       header=0).squeeze("columns")
                # get header data
                tmpHeader = [float(dataRead.name)]
                tmpHeader[1:] = dataRead
                dataRead = pd.Series(tmpHeader)

                # get state
                fileState = objFile.replace('.csv', '').replace('RRM2_', '')
                self.__fileState.append(fileState)
                tmpTaDict.update({fileState: dataRead})

            tmpTaDataM2.append(tmpTaDict)

        # base data
        self.__dataBase = dict(zip(self.__taName, tmpTaData))
        self.__dataBaseM2 = dict(zip(self.__taName, tmpTaDataM2))

        # add data
        self.__dataBaseAll = dict(
            zip(self.__dataBaseType, [self.__dataBase, self.__dataBaseM2]))

        self.__fileState = tuple(set(self.__fileState))

    def get_data_base(self) -> dict:
        """get the data base of RR_csv(Name --> State --> Data)"""
        return self.__dataBase

    def get_data_base_M2(self) -> dict:
        """get the data base of RR_csv(Name --> State --> Data) M2"""
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
"""
tmp = RRClass()
cw = tmp.get_data_base()['CW']
ht = tmp.get_data_base()['HT']
print(cw)
"""
