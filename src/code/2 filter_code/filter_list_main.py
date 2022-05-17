import os
from custom_filter_class import EcgFileFilter
from pandas import DataFrame as df

folderTree = ['CW', 'HT']
dataFolder = 'src\data'


folderFileName = dict()
for nameFolder in folderTree:
    name = os.path.join(os.path.abspath(dataFolder), nameFolder)

    try:
        lsDir = os.listdir(name)
        folderFilter = EcgFileFilter(nameFolder)

        for i in lsDir:
            folderFilter.add(os.path.join(dataFolder, nameFolder, i))

        folderFileName.update({nameFolder: folderFilter})

    except Exception as e:
        print(e)
        exit()

for key, val in folderFileName.items():
    val.formatPrint()
    val.outToFile('src\FilterOutput')