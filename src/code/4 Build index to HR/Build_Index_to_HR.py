import os
from pprint import pprint
import pandas as pd


def Cal_HR(inputList: list) -> list:
    reHR = []
    inputListSize = len(inputList)
    for index, val in enumerate(inputList):
        if index < inputListSize:
            tranHRPart = 60*200/(inputListSize[index+1]-val)
            reHR.append(tranHRPart)


pathLoc = 'src\FilterOutput'
names = ['CW', 'HT']
filePathType = 'simple'

for name in names:
    locCheck = os.path.join(pathLoc, name, filePathType)
    listName = None

    if os.path.isdir(locCheck):
        listName = os.listdir(locCheck)
        listName = [i.replace('.csv', '') for i in listName]
        pprint(listName)
