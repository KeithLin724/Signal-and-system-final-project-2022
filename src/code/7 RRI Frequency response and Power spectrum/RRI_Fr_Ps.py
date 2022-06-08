import os
from RR_Class import RRClass
from PJ_FFT_Algor import data_to_png, get_ppi

# open the folder
rrDataCenter = RRClass()
# rrDataBase = rrDataCenter.get_data_base()
rrDataBaseM2 = rrDataCenter.get_data_base_M2()
Dpi = get_ppi()

# output file folder name
outputFolderName = os.path.join('src',
                                'RRI Frequency response and Power spectrum')
if not os.path.exists(outputFolderName):
    os.mkdir(outputFolderName)

for name, stateOfFile in rrDataBaseM2.items():

    # make the branch Folder of the Ta name
    outputFolderNameBranch = os.path.join(outputFolderName, name)
    if not os.path.exists(outputFolderNameBranch):
        os.mkdir(outputFolderNameBranch)

    for state, data in stateOfFile.items():
        data_to_png(dataIn=data,
                    dataOutPath=outputFolderNameBranch,
                    dataFileName=f'{name}_{state}_FR_PS',
                    dpi=Dpi)
