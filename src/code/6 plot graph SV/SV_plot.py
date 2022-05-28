from copy import deepcopy
from PKG import *
import os

fileCenter = FileCenter()

dataType = fileCenter.get_file_type()
dataBase = fileCenter.get_data_basie()
dataName = fileCenter.get_data_name()  # TODO: get ta name
dpi = get_ppi()
#dataLoc = fileCenter.get_data_item_loc()

dataTaList = (dataBase[dataName[0]]['SV'], dataBase[dataName[1]]['SV'])
taDataDict = dict(zip(dataName, deepcopy(dataTaList)))

# save picture file path
mainFolder, saveFolder = 'src', 'SV graphs'

saveMainFolder = os.path.join(mainFolder, saveFolder)
if not os.path.exists(saveMainFolder):
    os.mkdir(saveMainFolder)

for name, varData in taDataDict.items():
    saveTaBranchPath = os.path.join(saveMainFolder, name)

    if not os.path.exists(saveTaBranchPath):
        os.mkdir(saveTaBranchPath)

    for svFileObj in varData:
        svFileObj.save_to_png(folderPath=saveTaBranchPath,
                              dpi=dpi)
    # test
# print(taDataDict)

# print()
