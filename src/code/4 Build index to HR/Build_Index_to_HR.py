# %%
import os
from pprint import pprint
import pandas as pd
from PKG import FileCenter, get_ppi
from rich import print
import matplotlib.pyplot as plt
#import numba as nb
# %%

# @nb.jit()


def Cal_HR(inputList: list) -> list:
    """_summary_
        index to HR function
    Returns:
        list: index to HR 
    """

    reHR = []
    inputListSize = len(inputList)
    for index, val in enumerate(inputList):
        if index + 1 < inputListSize:
            #diff = inputList[index+1]-val
            tranHRPart = 60.0*200.0/(inputList[index+1]-val)
            reHR.append(tranHRPart)

    return reHR


def save_to_png(folderPath: str, titleStr: str, data: pd.DataFrame, dpi: int = 100) -> None:
    """_summary_
        Save DataFrame to png function
    Args:
        folderPath (str): about save picture folder path 
        titleStr (str): about the picture title 
        data (pd.DataFrame): about the data about the picture
        dpi (int, optional): about the picture quality Defaults to 100.
    """
    plt.clf()

    data.plot(legend=True)
    titleStr = titleStr.capitalize()
    plt.title(titleStr)

    #fileName = titleStr + '_diff.png'
    saveFilePath = os.path.join(folderPath, f'{titleStr}_diff.png')
    plt.savefig(saveFilePath, dpi=dpi)

    plt.clf()
    plt.close()


# input file center
fileCenter = FileCenter()

names = fileCenter.get_data_name()
dataBasic = fileCenter.get_data_basie()
loc = fileCenter.get_data_item_loc()
filetype = fileCenter.get_file_type()

indexStr = 'index'
mainFolder = 'src'
saveFolder = 'index to HR with HR File Diff Picture'

dpi = get_ppi()

saveFolderPath = os.path.join(mainFolder, saveFolder)
if os.path.exists(saveFolderPath) == False:
    os.mkdir(saveFolderPath)


for name in names:
    indexFileListDataOri = dataBasic[name][indexStr]
    hrFileListDataOri = dataBasic[name]['HR']

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
    packIndexToHRAndOri = tuple(zip(hrFileListDataStateList,
                                    hrFileListData,
                                    indexFileListDataToHR))
    dataSaveDic = dict()
    for state, hrOri, indexToHR in packIndexToHRAndOri:
        dictTmp = {'origin HR': pd.Series(hrOri),
                   'index to HR': pd.Series(indexToHR)}

        dictTmp = pd.DataFrame(dictTmp)
        # print(dictTmp)
        dataSaveDic.update({state: dictTmp})

    print(len(dataSaveDic))

    print(dataSaveDic)

    nameSaveFolderPath = os.path.join(saveFolderPath, name)

    if os.path.exists(nameSaveFolderPath) == False:
        os.mkdir(nameSaveFolderPath)

    for state, pdDf in dataSaveDic.items():
        save_to_png(folderPath=nameSaveFolderPath,
                    titleStr=state,
                    data=pdDf,
                    dpi=dpi)

# print(packIndexToHRAndOri)

'''
indexP = pd.Series(indexFileListData[0])
indexP.plot(legend=True)
plt.show()
'''

# test
'''
fileDict = {'origin HR': hrFileListData[0],
            'index to HR': indexFileListDataToHR[0]}
testPartDP = pd.DataFrame(fileDict)
#testPartDP['origin HR'] = hrFileListData[0]
#testPartDP['index to HR'] = indexFileListDataToHR[0]
testPartDP.plot(legend=True)
print(testPartDP)
plt.show()
'''
