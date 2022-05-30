from os import path
from os.path import basename
from pandas import read_csv, Series
from matplotlib.pyplot import savefig, clf, close


class FileDataClass:
    def __init__(self, path: str) -> None:
        self.__fileName, self.__fromFolder = (basename(path),
                                              path.split(path))

        self.__fileData = read_csv(path,
                                   index_col=False,
                                   header=0).squeeze('columns')
        # print(self.__fileData)

        tmpHeader = [float(self.__fileData.name)]

        tmpHeader[1:] = self.__fileData
        self.__fileData = Series(tmpHeader)

        tmpNameList = self.__fileName.replace('.csv', '')
        self.__fileData.name = tmpNameList.replace('_', ' ')
        tmpNameList = tmpNameList.split('_')

        self.__name, self.__state, self.__dataType = tmpNameList

    def get_file_type_detail(self) -> tuple:
        '''get data type Name , state, Data Type'''
        return (self.__name, self.__state, self.__dataType)

    def get_file_data(self) -> Series:
        '''return the file data using Pandas Series type'''
        return self.__fileData

    def get_file_path(self) -> tuple:
        '''get file simple path'''
        return (self.__fileName, self.__fromFolder)

    def save_to_png(self, folderPath: str, dpi: int = 100) -> None:
        """_summary_
            This is a function that saves the file
        Args:
            folderPath (str): the folder path to save
            dpi (int, optional): about the save picture quality. Defaults to 100.
        """
        clf()

        self.__fileData.plot(legend=True, label=self.__fileData.name)
        saveFileName = self.__fileData.name.replace(' ', '_') + '.png'
        saveFilePath = path.join(folderPath, saveFileName)

        savefig(saveFilePath, dpi=dpi)
        clf()
        close()

    def __repr__(self) -> str:
        return f'FileDataClass Name :{self.__name}, DataType :{self.__dataType}, State :{self.__state}'


# DEBUG: test
# a = FileDataClass('src\data\CW\CW_baseline_SV.csv')

# tmp = a.get_file_data()

# pprint(tmp)

# print(os.path.exists('src\data\CW\CW_baseline_SV.csv'))
