from PKG import FileCenter
from PJ_FFT_Algor import Frequency_response_and_Power_spectrum_To_png, get_ppi
import os

Dpi = get_ppi()
# get data from data base
fileCenter = FileCenter()
dataBase = fileCenter.get_data_basie()
taName = fileCenter.get_data_name()

# get need data
filterDataBase = dataBase[taName[0]]['SV'], dataBase[taName[1]]['SV']
filterDataBase = dict(zip(taName, filterDataBase))

saveFolderPath = os.path.join('src',
                              'SV Frequency response and Power spectrum')
if not os.path.exists(saveFolderPath):
    os.mkdir(saveFolderPath)

for name, dataValue in filterDataBase.items():
    saveFolderPathBranch = os.path.join(saveFolderPath, name)
    if not os.path.exists(saveFolderPathBranch):
        os.mkdir(saveFolderPathBranch)

    for obj in dataValue:
        fileData = obj.get_file_data()
        _, state, _ = obj.get_file_type_detail()
        Frequency_response_and_Power_spectrum_To_png(
            dataIn=fileData,
            dataFileName=f'{name}_{state}',
            dataOutPath=saveFolderPathBranch,
            dpi=Dpi)
