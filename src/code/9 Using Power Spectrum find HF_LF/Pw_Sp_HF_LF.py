import os
from PKG import FileCenter
from RR_Class import RRClass
from numpy.fft import fft
import numpy as np
from rich import print
import pandas as pd


def power_spectrum_to_variance(dataIn: list) -> float:
    """_summary_
        This function make variance base on power spectrum
    Args:
        dataIn (list): power spectrum data

    Returns:
        float: variance
    """
    N = len(dataIn)

    yf = fft(dataIn)
    yf_pw = abs(yf)**2

    xf = np.linspace(0.0, 0.5, N // 2)

    dataPack = dict(zip(xf.tolist(), yf_pw[0:N // 2].tolist()))  # 0 to 0.5

    hfDataList, lfDataList = [], []

    for objHz, var in dataPack.items():
        if 0.04 <= objHz <= 0.15:
            lfDataList.append(var)
        if 0.15 <= objHz <= 0.40:
            hfDataList.append(var)

    hfVariances, lfVariances = np.var(hfDataList), np.var(lfDataList)

    return hfVariances / lfVariances


# open two data
fileCenter, rrCenter = FileCenter(), RRClass()

dataBase, rrDataBase, taNames = (fileCenter.get_data_basie(),
                                 rrCenter.get_data_base_M2(),
                                 fileCenter.get_data_name())

dataBaseSVList = [dataBase[Name]['SV'] for Name in taNames]
dataBaseSV = dict(zip(taNames, dataBaseSVList))

# save folder path
saveFolderPath = os.path.join('src', 'power spectrum Cal HF LF (SV and RRI)')
if not os.path.exists(saveFolderPath):
    os.mkdir(saveFolderPath)

for name in taNames:
    dataSV, dataRR = dataBaseSV[name], rrDataBase[name]

    dataSVAllVar = [
        power_spectrum_to_variance(dataIn=list(var.get_file_data()))
        for var in dataSV
    ]

    dataRRAllVar = [
        power_spectrum_to_variance(dataIn=list(var))
        for _, var in dataRR.items()
    ]

    indexName = list(dataRR.keys())

    df = pd.DataFrame({
        'SV': dataSVAllVar,
        'RRI': dataRRAllVar
    },
                      index=indexName)
    print(df)
    fileSavePath = os.path.join(saveFolderPath,
                                f'{name}_power_spectrum_SV_RRT.csv')
    df.to_csv(fileSavePath)
