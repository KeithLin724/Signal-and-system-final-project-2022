from rich import print
from copy import deepcopy
import os


class EcgFileFilter:
    def __init__(self, name: str) -> None:
        self.name = name
        STATIC_DIC = {'baseline': [],
                      'stage1': [],
                      'stage2': [],
                      'stage3': [],
                      'stage4': [],
                      'recovery': []}
        #tmpCopy = [STATIC_DIC for _ in range(3)]
        self.filterDic = {'HR': deepcopy(STATIC_DIC),
                          'index': deepcopy(STATIC_DIC),
                          'SV': deepcopy(STATIC_DIC)}

    def add(self, fileName: str):
        tmpFileName = fileName
        fileSplit = fileName.replace('.csv', '').split('_')
        if fileSplit[0] == self.name:
            if fileSplit[2] in self.filterDic:
                if fileSplit[1] in self.filterDic[fileSplit[2]]:

                    self.filterDic[fileSplit[2]
                                   ][fileSplit[1]].append(tmpFileName)
                    self.filterDic[fileSplit[2]][fileSplit[1]].append(
                        os.path.abspath(tmpFileName))
                else:
                    self.filterDic[fileSplit[2]].update(
                        {fileSplit[1]: [tmpFileName, os.path.abspath(tmpFileName)]})

        # print(fileSplit)

    def __str__(self) -> str:
        return str(self.filterDic)

    def formatPrint(self) -> None:
        print(self.name)
        print(self.filterDic)

    def outToFile(self, folderSave: str) -> None:
        if os.path.exists(folderSave) == False:
            os.mkdir(folderSave)
        folderSave = os.path.join(folderSave, self.name)
        os.mkdir(folderSave)
        PATHTYPE = ['simple', 'absolute']
        simPath, absPath = os.path.join(
            folderSave, PATHTYPE[0]), os.path.join(folderSave, PATHTYPE[1])

        os.mkdir(simPath)
        os.mkdir(absPath)
        for typeKey, stateValue in self.filterDic.items():
            fileNameTmp = typeKey+'.txt'
            with open(file=os.path.join(simPath, fileNameTmp), mode='w') as simFile, \
                    open(file=os.path.join(absPath, fileNameTmp), mode='w') as absFile:
                for _, filePath in stateValue.items():
                    simFile.write(filePath[0]+'\n')
                    absFile.write(filePath[1]+'\n')


#a = EcgFileFilter('Hello world')
# print(a)
