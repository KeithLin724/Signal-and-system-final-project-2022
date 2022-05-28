from copy import deepcopy
from PKG import *
import pandas as pd
from rich import print
import os

# open data
fileCenter = FileCenter()
# get data
dataBase = fileCenter.get_data_basie()
dataName = fileCenter.get_data_name()
dataType = fileCenter.get_file_type()
dpi = get_ppi()


def to_rr_interval(dataHR: list) -> list:
    """_summary_

    Args:
        dataHR (list):input the HR list data 

    Returns:
        list: about the rr interval (type of float)
    """

    return [60/float(i) for i in dataHR]


mainFolder, branchFolder = 'src', 'RR Data'
saveMainFolder = os.path.join(mainFolder, branchFolder)
# save folder
if not os.path.exists(saveMainFolder):
    os.mkdir(saveMainFolder)

taData = (dataBase[dataName[0]]['HR'], dataBase[dataName[1]]['HR'])
taDataDict = dict(zip(dataName, taData))
dataStruct = []

dataChangeDict = {dataName[0]: deepcopy(dataStruct),
                  dataName[1]: deepcopy(dataStruct)}

for taName, valDataList in taDataDict.items():
    for fileObj in valDataList:
        tmpFileList = fileObj.get_file_data()
        tmpFileList = sorted(tmpFileList)
        _, fileState, _ = fileObj.get_file_type_detail()
        tranToRR = to_rr_interval(tmpFileList)

        # print(tranToRR)
        #print(len(tmpFileList) == len(tranToRR))
        tmpDf = pd.DataFrame({'Heart Beats': tmpFileList,
                              'RRI Value': tranToRR})
        dataChangeDict[taName].append((fileState, tmpDf))


# check the data
print(dataChangeDict)
# to file

for taName, valTuples in dataChangeDict.items():
    savePath = os.path.join(saveMainFolder, taName)
    if not os.path.exists(savePath):
        os.mkdir(savePath)

    for state, dataDf in valTuples:
        saveBranchFolder = os.path.join(savePath, state)

        if not os.path.exists(saveBranchFolder):
            os.mkdir(saveBranchFolder)

        title = f'RR-interval {state}'

        save_to_png(folderPath=saveBranchFolder,
                    titleStr=title,
                    x_ticks=True,
                    data=dataDf,
                    dpi=dpi)
        # save file name
        fileCSVSavePath = os.path.join(saveBranchFolder, f'{title}.csv')
        dataDf.to_csv(fileCSVSavePath, index=False)
