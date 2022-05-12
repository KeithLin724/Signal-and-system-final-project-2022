import os
import pandas as pd
from pprint import pprint


class FileDataClass:
    def __init__(self, path: str) -> None:
        self.__fileName = os.path.basename(path)
        self.__fromFolder = os.path.split(path)

        self.__fileData = pd.read_csv(path,
                                      index_col=False,
                                      squeeze=True)

        tmpNameList = self.__fileName.replace('.csv', '').split('_')
        self.__name = tmpNameList[0]
        self.__state = tmpNameList[1]
        self.__dataType = tmpNameList[2]

    def get_file_type_deatil(self) -> tuple:
        return (self.__name, self.__state, self.__dataType)

    def get_file_data(self) -> pd.Series:
        return self.__fileData

    def get_file_path(self) -> tuple:
        return (self.__fileName, self.__fromFolder)


# test
a = FileDataClass(
    'src\data\CW\CW_baseline_SV.csv')

tmp = a.get_file_data()

pprint(tmp)

print(os.path.exists('src\data\CW\CW_baseline_SV.csv'))
