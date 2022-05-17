from copy import deepcopy
import os
from pprint import pprint
from file_data_class import FileDataClass

#dpi = get_ppi()


class FileCenter:
    def __init__(self) -> None:
        self.__pathLoc = 'src\FilterOutput'

        self.__names = ['CW', 'HT']
        self.__filePathType = 'simple'


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

        objList = [FileDataClass(i) for i in simplePath]
        for i in objList:
            name, _, typeName = i.get_file_type_detail()
            print(name, _, typeName)
            dataPathClass[name][typeName].append(i)

pprint(dataPathClass)
