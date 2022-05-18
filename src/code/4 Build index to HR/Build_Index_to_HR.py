
import os
from pprint import pprint
import pandas as pd
from PKG import FileCenter, FileDataClass
from rich import print
import matplotlib.pyplot as plt


def Cal_HR(inputList: list) -> list:
    reHR = []
    inputListSize = len(inputList)
    for index, val in enumerate(inputList):
        if index + 1 < inputListSize:
            diff = inputList[index+1]-val
            tranHRPart = 60.0*200.0/(inputList[index+1]-val)
            reHR.append(tranHRPart)

    return reHR


# input file center
fileCenter = FileCenter()

names = fileCenter.get_data_name()
dataBasic = fileCenter.get_data_basie()
loc = fileCenter.get_data_item_loc()
filetype = fileCenter.get_file_type()

indexStr = 'index'
name = names[0]
indexFileListData = dataBasic[name][indexStr]
hrFileListData = dataBasic[name]['HR']

indexFileListData = [i.get_file_data() for i in indexFileListData]
hrFileListData = [i.get_file_data() for i in hrFileListData]


indexFileListDataToHR = [Cal_HR(i) for i in indexFileListData]


print(set([len(i) for i in indexFileListDataToHR]))
print(set([len(i) for i in hrFileListData]))

# test
testPartDP = pd.DataFrame()
testPartDP['origin HR'] = hrFileListData[0]
testPartDP['index to HR'] = indexFileListDataToHR[0]
testPartDP.plot(legend=True)
print(testPartDP)
plt.show()
