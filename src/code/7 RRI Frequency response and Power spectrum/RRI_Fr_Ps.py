import os
from RR_Class import RRClass
from PJ_FFT_Algor import Frequency_response_and_Power_spectrum_To_png, get_ppi, PowerSpectrum
import pandas as pd

# open the folder
rrDataCenter = RRClass()
rrDataBaseM2, Dpi = rrDataCenter.get_data_base_M2(), get_ppi()

# output file folder name
outputFolderName = os.path.join('src',
                                'RRI Frequency response and Power spectrum')
if not os.path.exists(outputFolderName):
    os.mkdir(outputFolderName)

dataSave, stateList = dict(), []

for name, stateOfFile in rrDataBaseM2.items():

    # make the branch Folder of the Ta name
    outputFolderNameBranch = os.path.join(outputFolderName, name)
    if not os.path.exists(outputFolderNameBranch):
        os.mkdir(outputFolderNameBranch)

    taTotalPowerList = []

    for state, data in stateOfFile.items():
        Frequency_response_and_Power_spectrum_To_png(
            dataIn=data,
            dataOutPath=outputFolderNameBranch,
            dataFileName=f'{name}_{state}_FR_PS',
            dpi=Dpi)

        # add the state
        if state not in stateList:
            stateList.append(state)

        # cal the total power
        pw = PowerSpectrum(data)
        taTotalPowerList.append(pw.total_power())

    # end of the loop
    dataSave.update({name: taTotalPowerList})

# save the total power data to the output csv file
dataSave['CW'].append(-1)
df = pd.DataFrame(dataSave, index=stateList)
savePath = os.path.join(outputFolderName, 'Total Power (RRI)(Unit dB).csv')
df.to_csv(savePath)
