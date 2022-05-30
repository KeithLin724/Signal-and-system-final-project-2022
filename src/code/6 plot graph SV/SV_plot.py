from copy import deepcopy
from PKG import FileCenter, get_ppi

import os

# TODO: open data
fileCenter = FileCenter()

# TODO: get ta name
dataType, dataBase, dataName, dpi = (fileCenter.get_file_type(),
                                     fileCenter.get_data_basie(),
                                     fileCenter.get_data_name(),
                                     get_ppi())


dataTaList = (dataBase[dataName[0]]['SV'], dataBase[dataName[1]]['SV'])
taDataDict = dict(zip(dataName, deepcopy(dataTaList)))

# save picture file path
mainFolder, saveFolder = 'src', 'SV graphs'

saveMainFolder = os.path.join(mainFolder, saveFolder)
if not os.path.exists(saveMainFolder):
    os.mkdir(saveMainFolder)

# TODO: Save file
for name, varData in taDataDict.items():
    saveTaBranchPath = os.path.join(saveMainFolder, name)

    if not os.path.exists(saveTaBranchPath):
        os.mkdir(saveTaBranchPath)

    for svFileObj in varData:
        svFileObj.save_to_png(folderPath=saveTaBranchPath,
                              dpi=dpi)
