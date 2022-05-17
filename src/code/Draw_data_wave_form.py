

from copy import deepcopy

from file_data_class import FileDataClass  # import the File Date
import matplotlib.pyplot as plt  # about plot the graph
import os  # read file in lib
from pprint import pprint
import pandas as pd


pathLoc = 'src\FilterOutput'
names = ['CW', 'HT']
filePathType = 'simple'

dataPathClass = dict()
emptyList = [[], [], []]
locCheckDict = dict()
for name in names:
    locCheck = os.path.join(pathLoc, name, filePathType)
    listOfFileName = None

    if os.path.isdir(locCheck):
        listOfFileName = os.listdir(locCheck)
        listOfName = [i.replace('.txt', '') for i in listOfFileName]
        dicZipList = dict(zip(listOfName, deepcopy(emptyList)))
        # pprint(listOfName)
        # pprint(dicZipList)
        dataPathClass.update({name: dicZipList})

        locCheckDict.update(
            {name: [os.path.join(locCheck, i) for i in listOfFileName]})


pprint(dataPathClass)
pprint(locCheckDict)

for nameC, filePaths in locCheckDict.items():
    for filePath in filePaths:
        simplePath = []
        with open(filePath, mode='r') as f:
            simplePath = [i.replace('\n', '') for i in list(f.readlines())]
            # pprint(simplePath)
        objList = [FileDataClass(i) for i in simplePath]
        for i in objList:
            name, _, typeName = i.get_file_type_deatil()
            print(name, _, typeName)
            dataPathClass[name][typeName].append(i)


saveFolderName = os.path.join('src', 'file Picture')
if os.path.exists(saveFolderName) == False:
    os.mkdir(saveFolderName)

for namePart, dataDict in dataPathClass.items():

    outSaveFolderName = os.path.join(saveFolderName, namePart)

    if os.path.exists(outSaveFolderName) == False:
        os.mkdir(outSaveFolderName)

    for typeName, objFile in dataDict.items():
        insideSaveFolderName = os.path.join(outSaveFolderName, typeName)

        if os.path.exists(insideSaveFolderName) == False:
            os.mkdir(insideSaveFolderName)

        for i in objFile:
            i.save_to_png(folderPath=insideSaveFolderName)
