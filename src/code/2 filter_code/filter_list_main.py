"""
Title:filter list main
Written By KYLiN
This is code for make filter data
Date: 18/5/2022
"""

import os
from custom_filter_class import EcgFileFilter

folderTree = ["CW", "HT"]
dataFolder = "src\\data"


folderFileName = dict()
for nameFolder in folderTree:
    name = os.path.join(os.path.abspath(dataFolder), nameFolder)

    try:
        lsDir, folderFilter = (os.listdir(name), EcgFileFilter(nameFolder))

        for i in lsDir:
            folderFilter.add(os.path.join(dataFolder, nameFolder, i))

        folderFileName.update({nameFolder: folderFilter})

    except Exception as e:
        print(e)
        exit()

for key, val in folderFileName.items():
    # val.formatPrint()
    print(val)
    val.outToFile("src\\FilterOutput")
