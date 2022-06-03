from PKG import FileCenter, get_ppi, save_to_png
from RR_Class import RRClass
from rich import print
import pandas as pd
import os

# save folder name
mainFolder, mainSaveFolder = 'src', 'All Picture Mix'
mainSaveFolderPath = os.path.join(mainFolder, mainSaveFolder)
if not os.path.exists(mainSaveFolderPath):
    os.mkdir(mainSaveFolderPath)

Dpi = get_ppi()

# data of main
fileCenter = FileCenter()
dataBase, taNames, typeOfName = (fileCenter.get_data_basie(),
                                 fileCenter.get_data_name(),
                                 fileCenter.get_file_type())
saveFolder = 'Source Folder'
saveFolderPath = os.path.join(mainSaveFolderPath, saveFolder)
if not os.path.exists(saveFolderPath):
    os.mkdir(saveFolderPath)

for name in taNames:
    # NOTE: open folder for save (main source)
    saveFolderBranch = os.path.join(saveFolderPath, name)
    if not os.path.exists(saveFolderBranch):
        os.mkdir(saveFolderBranch)

    for name, taDataDictList in dataBase.items():
        for dataFileType, fileList in taDataDictList.items():
            df = pd.DataFrame()

            for dataObj in fileList:
                _, state, _ = dataObj.get_file_type_detail()
                df[state] = dataObj.get_file_data()

            save_to_png(folderPath=saveFolderBranch,
                        titleStr=f'{name}_{dataFileType}_all_graph',
                        data=df,
                        dpi=Dpi)

print(dataBase)

# NOTE: about the rr data
rrDataCenter = RRClass()
rrDataBaseType = rrDataCenter.get_data_base_type()
rrDataBase = rrDataCenter.get_data_base_all()
rrSavePath = 'RR All Graph'  # NOTE: this is a save path for the rr data

saveRRSavePath = os.path.join(mainSaveFolderPath, rrSavePath)
if not os.path.exists(saveRRSavePath):
    os.mkdir(saveRRSavePath)

for rrBaseType, varDataBase in rrDataBase.items():

    for name, dataStateAll in varDataBase.items():
        df = pd.DataFrame(dataStateAll)
        # save png
        save_to_png(folderPath=saveRRSavePath,
                    titleStr=f'{rrBaseType}_{name}_RRI',
                    data=df,
                    dpi=Dpi)

print(rrDataBase)
