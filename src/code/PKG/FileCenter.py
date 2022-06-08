from .file_data_class import FileDataClass
from os import path, listdir
from pandas import DataFrame
from copy import deepcopy
from ctypes import windll
from pprint import pformat
from matplotlib.pyplot import savefig, clf, close, title, xlabel, ylabel


def get_ppi():
    """get the dpi function"""
    LOGPIXELSX, LOGPIXELSY, user32 = (88, 90, windll.user32)

    user32.SetProcessDPIAware()
    dc = user32.GetDC(0)
    pix_per_inch = windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
    user32.ReleaseDC(0, dc)
    return pix_per_inch


# dpi = get_ppi()


def save_to_png(folderPath: str,
                titleStr: str,
                data,
                xLabel: str = None,
                yLabel: str = None,
                dpi: int = 100) -> None:
    """_summary_
        Save DataFrame to png function
    Args:
        folderPath (str): about save picture folder path 
        titleStr (str): about the picture title 
        data : about the data about the picture
        xLabel (str, optional): set x Label Name Defaults to None.
        yLabel (str, optional): set y Label Name Defaults to None.
        dpi (int, optional): about the picture quality Defaults to 100.
    """

    clf()

    data.plot(legend=True)
    # titleStr = titleStr.capitalize()
    title(titleStr)

    # fileName = titleStr + '_diff.png'
    saveFilePath = path.join(folderPath, f"{titleStr}_diff.png")

    if xLabel is not None:
        xlabel(xLabel)

    if yLabel is not None:
        ylabel(yLabel)

    savefig(saveFilePath, dpi=dpi)
    clf()
    close()


class FileCenter:
    """_summary_

        This is a class for control the file 

        Base on the class of FileDataClass 
    """

    def __init__(self) -> None:
        self.__pathLoc = "src\\FilterOutput"

        self.__names = ["CW", "HT"]
        self.__filePathType = "simple"
        self.__dataBasie = dict()
        self.__fileType = []
        emptyList = [[], [], []]
        self.__locCheckDict = dict()

        for name in self.__names:
            locCheck = path.join(self.__pathLoc, name, self.__filePathType)

            if not path.exists(locCheck) and not path.isdir(locCheck):
                exit()

            listOfFileName = listdir(locCheck)
            listOfName = [i.replace(".txt", "") for i in listOfFileName]

            dicZipList = dict(zip(listOfName, deepcopy(emptyList)))

            self.__fileType.extend(listOfName)

            self.__dataBasie.update({name: dicZipList})

            self.__locCheckDict.update(
                {name: [path.join(locCheck, i) for i in listOfFileName]})

        for _, filePaths in self.__locCheckDict.items():
            for filePath in filePaths:
                try:
                    with open(filePath, mode='r') as f:
                        simplePath = [
                            i.replace("\n", "") for i in list(f.readlines())
                        ]

                except Exception as e:
                    print(e)
                    exit()

                objList = [FileDataClass(i) for i in simplePath]
                for i in objList:
                    name, _, typeName = i.get_file_type_detail()
                    # print(name, _, typeName)
                    self.__dataBasie[name][typeName].append(i)

        self.__fileType = tuple(set(self.__fileType))

    def __str__(self) -> str:
        return pformat(self.__dataBasie)

    def get_data_basie(self) -> dict:
        """get data base name->FileType->state"""
        return self.__dataBasie

    def get_data_name(self) -> tuple:
        """get data TA name from data"""
        return self.__names

    def get_data_item_loc(self) -> dict:
        return self.__locCheckDict

    def get_file_type(self) -> tuple:
        """get file type"""
        return self.__fileType

    def get_file_of_name(self, name: str) -> dict:
        """get dict using name """
        return self.__dataBasie[name] if name in self.__names else dict()

    def get_file_of_type(self, name: str, typeOfName: str) -> list:
        """get file using name and type"""
        return (self.__dataBasie[name][typeOfName] if name in self.__names
                and typeOfName in self.__fileType else dict())

    """
    def __repr__(self) -> str:
        return str()
    """
