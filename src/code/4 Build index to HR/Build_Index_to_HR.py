
import os
from pprint import pprint
import pandas as pd
from PKG import FileCenter


def Cal_HR(inputList: list) -> list:
    reHR = []
    inputListSize = len(inputList)
    for index, val in enumerate(inputList):
        if index < inputListSize:
            tranHRPart = 60*200/(inputListSize[index+1]-val)
            reHR.append(tranHRPart)


fileCenter = FileCenter()
dataBasic = fileCenter.get_data_basie()

pprint(dataBasic)
