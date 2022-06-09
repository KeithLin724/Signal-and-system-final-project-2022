from .file_data_class import FileDataClass
from os import path, listdir
import pandas as pd
from copy import deepcopy
import ctypes
from pprint import pformat
from matplotlib import pyplot as plt


def get_ppi():
    '''get the dpi function'''
    LOGPIXELSX, LOGPIXELSY, user32 = (88, 90, ctypes.windll.user32)

    user32.SetProcessDPIAware()
    dc = user32.GetDC(0)
    pix_per_inch = ctypes.windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
    user32.ReleaseDC(0, dc)
    return pix_per_inch


#dpi = get_ppi()


def save_to_png(folderPath: str,
                titleStr: str,
                data: pd.DataFrame,
                x_ticks: bool = False,
                dpi: int = 100) -> None:
    """_summary_
        Save DataFrame to png function
    Args:
        folderPath (str): about save picture folder path 
        titleStr (str): about the picture title 
        data (pd.DataFrame): about the data about the picture
        x_ticks (bool, optional): is use the first columns to x axis
        dpi (int, optional): about the dpi of the picture
    """

    plt.clf()
    if x_ticks:
        data.set_index(data.columns.values[0]).plot(legend=True)
    else:
        data.plot(legend=True)
    # titleStr = titleStr.capitalize()
    plt.title(titleStr)

    #fileName = titleStr + '_diff.png'
    saveFilePath = path.join(folderPath, f'{titleStr}.png')
    plt.savefig(saveFilePath, dpi=dpi)

    plt.clf()
    plt.close()


class FileCenter:

    def __init__(self) -> None:
        self.__pathLoc = 'src\\FilterOutput'

        self.__names = ['CW', 'HT']
        self.__filePathType = 'simple'
        self.__dataBasie = dict()
        self.__fileType = []
        emptyList = [[], [], []]
        self.__locCheckDict = dict()
        #self.__dpi = get_ppi()

        for name in self.__names:
            locCheck = path.join(self.__pathLoc, name, self.__filePathType)
            #listOfFileName = None

            if not path.exists(locCheck) and not path.isdir(locCheck):
                exit()

            listOfFileName = listdir(locCheck)
            listOfName = [i.replace('.txt', '') for i in listOfFileName]

            dicZipList = dict(zip(listOfName, deepcopy(emptyList)))

            self.__fileType.extend(listOfName)

            self.__dataBasie.update({name: dicZipList})

            self.__locCheckDict.update(
                {name: [path.join(locCheck, i) for i in listOfFileName]})

        for _, filePaths in self.__locCheckDict.items():
            for filePath in filePaths:
                #simplePath = []

                try:
                    with open(filePath, mode='r') as f:
                        simplePath = [
                            i.replace('\n', '') for i in list(f.readlines())
                        ]
                except Exception as e:
                    print(e)
                    exit()

                objList = [FileDataClass(i) for i in simplePath]
                for i in objList:
                    name, _, typeName = i.get_file_type_detail()
                    #print(name, _, typeName)
                    self.__dataBasie[name][typeName].append(i)

        self.__fileType = tuple(set(self.__fileType))

    def __str__(self) -> str:
        return pformat(self.__dataBasie)

    def get_data_basie(self) -> dict:
        return self.__dataBasie

    def get_data_name(self) -> tuple:
        '''get data TA name from data'''
        return self.__names

    def get_data_item_loc(self) -> dict:
        return self.__locCheckDict

    def get_file_type(self) -> tuple:
        '''get file type'''
        return self.__fileType

    '''
    def __repr__(self) -> str:
        return str()
    '''


# debug
#tmp = FileCenter()
# print(tmp)
