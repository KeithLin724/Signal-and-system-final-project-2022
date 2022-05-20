from copy import deepcopy
import ctypes
from pprint import pformat
from .file_data_class import FileDataClass
from os import path, listdir


def get_ppi():
    '''get the dpi function'''
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    dc = user32.GetDC(0)
    pix_per_inch = ctypes.windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
    user32.ReleaseDC(0, dc)
    return pix_per_inch

#dpi = get_ppi()


class FileCenter:
    def __init__(self) -> None:
        self.__pathLoc = 'src\FilterOutput'

        self.__names = ['CW', 'HT']
        self.__filePathType = 'simple'
        self.__dataBasie = dict()
        self.__fileType = []
        emptyList = [[], [], []]
        self.__locCheckDict = dict()
        #self.__dpi = get_ppi()

        for name in self.__names:
            locCheck = path.join(self.__pathLoc, name, self.__filePathType)
            listOfFileName = None

            if path.isdir(locCheck):
                listOfFileName = listdir(locCheck)
                listOfName = [i.replace('.txt', '') for i in listOfFileName]

                dicZipList = dict(zip(listOfName, deepcopy(emptyList)))

                self.__fileType.extend(listOfName)

                self.__dataBasie.update({name: dicZipList})

                self.__locCheckDict.update(
                    {name: [path.join(locCheck, i) for i in listOfFileName]})

        for _, filePaths in self.__locCheckDict.items():
            for filePath in filePaths:
                simplePath = []
                with open(filePath, mode='r') as f:
                    simplePath = [i.replace('\n', '')
                                  for i in list(f.readlines())]

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
