# %%
import os
from pprint import pprint
import numpy as np
import pandas as pd
from PKG import FileCenter, get_ppi
from rich import print
import matplotlib.pyplot as plt
# %%


def Cal_HR(inputList: list) -> list:
    """_summary_
        index to HR function
    Returns:
        list: index to HR 
    """

    inputListSize = len(inputList)

    return [
        tranHRPart := 60.0 * 200.0 / (inputList[index + 1] - val)
        for index, val in enumerate(inputList) if index + 1 < inputListSize
    ]


# input file center
fileCenter = FileCenter()

names, dataBasic, loc, filetype = (fileCenter.get_data_name(),
                                   fileCenter.get_data_basie(),
                                   fileCenter.get_data_item_loc(),
                                   fileCenter.get_file_type())

indexStr, mainFolder, saveFolder = ("index", "src",
                                    "index to HR with HR File Diff")

dpi = get_ppi()

saveFolderPath = os.path.join(mainFolder, saveFolder)
if not os.path.exists(saveFolderPath):
    os.mkdir(saveFolderPath)

for name in names:
    indexFileListDataOri = dataBasic[name][indexStr]
    hrFileListDataOri = dataBasic[name]["HR"]

    # save file

    # origin data
    indexFileListData = [i.get_file_data() for i in indexFileListDataOri]

    hrFileListData = [i.get_file_data() for i in hrFileListDataOri]
    hrFileListDataState = [i.get_file_type_detail() for i in hrFileListDataOri]
    hrFileListDataStateList = [i for _, i, _ in hrFileListDataState]
    print(hrFileListDataStateList)

    # tran
    indexFileListDataToHR = [Cal_HR(i) for i in indexFileListData]

    # check length is same
    print(set([len(i) for i in indexFileListDataToHR]))
    print(set([len(i) for i in hrFileListData]))

    # pack it
    packIndexToHRAndOri = tuple(
        zip(hrFileListDataStateList, hrFileListData, indexFileListDataToHR))

    # dataSaveDic = dict()
    dataSaveDic = []
    for state, hrOri, indexToHR in packIndexToHRAndOri:

        dictTmp = pd.DataFrame({
            "origin HR": pd.Series(hrOri),
            "index to HR": pd.Series(indexToHR)
        })

        dataSaveDic.append((state, dictTmp))

    # create save folder
    nameSaveFolderPath = os.path.join(saveFolderPath, name)
    if not os.path.exists(nameSaveFolderPath):
        os.mkdir(nameSaveFolderPath)

    #make all in one
    plt.figure(figsize=(16, 12))
    colNumber = 2 if len(dataSaveDic) <= 6 else 3

    for index, val in enumerate(dataSaveDic):
        state, pdDf = val
        y, x = index // 3, index % 3
        colName = list(pdDf.columns)

        xScale = np.linspace(0, len(pdDf[colName[0]].tolist()),
                             len(pdDf[colName[0]].tolist()))
        plt.subplot(colNumber, 3, index + 1)
        plt.plot(xScale, pdDf[colName[0]].tolist(), label=colName[0])
        plt.plot(xScale, pdDf[colName[1]].tolist(), label=colName[1])

        plt.title(state)
        plt.xlabel('time (s)')
        plt.ylabel('HR Value')
        plt.grid()
        plt.legend()

    savePath = os.path.join(nameSaveFolderPath,
                            f'{name}_Index_HR_DIFF_AIO.png')
    plt.tight_layout()
    plt.savefig(savePath, dpi=dpi)
