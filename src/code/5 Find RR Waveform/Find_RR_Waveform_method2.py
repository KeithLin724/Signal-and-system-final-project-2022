from copy import deepcopy
from PKG import *
import pandas as pd
from rich import print
import os

# open data
fileCenter = FileCenter()
# get data
dataBase, dataName, dataType, dpi = (
    fileCenter.get_data_basie(),
    fileCenter.get_data_name(),
    fileCenter.get_file_type(),
    get_ppi(),
)


def to_rr_interval(dataHR: list) -> list:
    """_summary_
        let the HR data to be a RR interval
    Args:
        dataHR (list):input the HR list data 

    Returns:
        list: about the rr interval (type of float)
    """

    lstSize = len(dataHR)

    return [
        float(dataHR[index + 1]) - float(var) if index + 1 < lstSize
        and float(dataHR[index + 1]) - float(var) > 0 else 0
        for index, var in enumerate(dataHR)
    ]


# about the path
mainFolder, branchFolder = 'src', 'RR Data Method 2'

saveMainFolder, saveRrCSVFolder = (
    os.path.join(mainFolder, branchFolder),
    os.path.join(mainFolder, "RRM2_csv"),
)

# save folder
if not os.path.exists(saveMainFolder):
    os.mkdir(saveMainFolder)

if not os.path.exists(saveRrCSVFolder):
    os.mkdir(saveRrCSVFolder)

taData = (dataBase[dataName[0]]["index"], dataBase[dataName[1]]["index"])
taDataDict = dict(zip(dataName, taData))
dataStruct = []

# make the dataChange for save the tuple data (file state , DataFrame and RR data)
dataChangeDict = {
    dataName[0]: deepcopy(dataStruct),
    dataName[1]: deepcopy(dataStruct)
}

for taName, valDataList in taDataDict.items():
    for fileObj in valDataList:
        # get data from the file
        tmpFileList = fileObj.get_file_data()
        #tmpFileList = sorted(tmpFileList)  # sort data

        _, fileState, _ = fileObj.get_file_type_detail()
        tranToRR = to_rr_interval(tmpFileList)
        '''
        tmpDf = pd.DataFrame({
            "Heart Beats": tmpFileList,
            "RRI Value": tranToRR
        })#
        '''
        RRSeries = pd.Series(tranToRR)

        # save data
        dataChangeDict[taName].append((
            fileState,  # the state of the file
            # tmpDf,  # Data Frame of the RR and Heart Beats
            RRSeries,
        ))  # RR Series (for other code )

# check the data
print(dataChangeDict)

# to file
for taName, valTuples in dataChangeDict.items():

    # open save file path
    savePath = os.path.join(saveMainFolder, taName)
    if not os.path.exists(savePath):
        os.mkdir(savePath)

    # save for rr csv file
    rrCSVPath = os.path.join(saveRrCSVFolder, taName)
    if not os.path.exists(rrCSVPath):
        os.mkdir(rrCSVPath)

    for state, RRdata in valTuples:
        saveBranchFolder = os.path.join(savePath, state)

        if not os.path.exists(saveBranchFolder):
            os.mkdir(saveBranchFolder)

        title = f"RR-interval {state}"  # about the file name

        # Data Frame to png
        save_to_png(
            folderPath=saveBranchFolder,
            titleStr=title,
            x_ticks=False,
            data=RRdata,
            labelName=f'rr interval {state}',
            dpi=dpi,
        )

        # save file name
        fileCSVSavePath = os.path.join(saveBranchFolder, f"{title}.csv")
        RRdata.to_csv(fileCSVSavePath, index=False)

        rrCSVFilePath = os.path.join(rrCSVPath, f"RRM2_{state}.csv")
        RRdata.to_csv(rrCSVFilePath, index=False)
