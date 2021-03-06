import os
import pandas as pd
import matplotlib.pyplot as plt


class FileDataClass:

    def __init__(self, path: str) -> None:
        self.__fileName = os.path.basename(path)
        self.__fromFolder = os.path.split(path)

        self.__fileData = pd.read_csv(
            path,
            index_col=False,
            # squeeze=True,
            header=0).squeeze('columns')
        # print(self.__fileData)

        tmpHeader = [float(self.__fileData.name)]

        tmpHeader[1:] = self.__fileData
        self.__fileData = pd.Series(tmpHeader)

        tmpNameList = self.__fileName.replace('.csv', '')
        self.__fileData.name = tmpNameList.replace('_', ' ')
        tmpNameList = tmpNameList.split('_')
        '''
        self.__name = tmpNameList[0]
        self.__state = tmpNameList[1]
        self.__dataType = tmpNameList[2]
        '''
        self.__name, self.__state, self.__dataType = tmpNameList

    def get_file_type_detail(self) -> tuple:
        return (self.__name, self.__state, self.__dataType)

    def get_file_data(self) -> pd.Series:
        return self.__fileData

    def get_file_path(self) -> tuple:
        return (self.__fileName, self.__fromFolder)

    def save_to_png(self, folderPath: str, dpi: int = 100) -> None:
        plt.clf()

        self.__fileData.plot(legend=True, label=self.__fileData.name)
        saveFileName = self.__fileData.name.replace(' ', '_') + '.png'
        saveFilePath = os.path.join(folderPath, saveFileName)
        plt.xlabel('time (s)')
        plt.ylabel(f'{self.__dataType} values')

        plt.savefig(saveFilePath, dpi=dpi)

        plt.clf()
        plt.close()

    def __repr__(self) -> str:
        return f'FileDataClass Name :{self.__name}, DataType :{self.__dataType}, State :{self.__state}'


# DEBUG: test
# a = FileDataClass('src\data\CW\CW_baseline_SV.csv')

# tmp = a.get_file_data()

# pprint(tmp)

# print(os.path.exists('src\data\CW\CW_baseline_SV.csv'))
