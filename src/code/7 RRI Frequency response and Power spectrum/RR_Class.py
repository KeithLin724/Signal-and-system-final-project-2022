import os
import pandas as pd
from rich import print


class RRClass:
    """_summary_
    
        This a class of RR classes
        read the folder about the RR data (.csv file) 
    """

    def __init__(self) -> None:

        self.__mainFolderName, self.__folderName = "src", "RR_csv"
        self.__taName = ("CW", "HT")
        self.__fileState = []
        self.__dataBase = dict()
        tmpTaData = []
        findPath = os.path.join(self.__mainFolderName, self.__folderName)

        # TODO: this path is it exists
        if not os.path.exists(findPath) and not os.path.isdir(findPath):
            print(f"path is not found\nPath : {tmpPath}")
            exit()

        for taName in self.__taName:
            tmpPath = os.path.join(findPath, taName)

            if not os.path.exists(tmpPath):
                print(f"path is not found\nPath : {tmpPath}")
                exit()

            # TODO: Read the under folder file
            listOfFileName = os.listdir(tmpPath)
            tmpTaDict = dict()

            for objFile in listOfFileName:
                filePath = os.path.join(tmpPath, objFile)
                dataRead = pd.read_csv(filePath, index_col=False,
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

        self.__dataBase = dict(zip(self.__taName, tmpTaData))
        self.__fileState = tuple(set(self.__fileState))

    def get_data_base(self) -> dict:
        """get the data base of RR_csv(Name --> State --> Data)"""
        return self.__dataBase

    def get_ta_name(self) -> tuple:
        """get ta name"""
        return self.__taName

    def get_state_menu(self) -> tuple:
        """get file state list"""
        return self.__fileState


# debug
"""
tmp = RRClass()
cw = tmp.get_data_base()['CW']
ht = tmp.get_data_base()['HT']
print(cw)
"""
