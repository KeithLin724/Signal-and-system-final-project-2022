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

    def add(self, fileSimPath: str):
        'add file path in data structs function'
        tmpSimPath = fileSimPath

        tmpSimPathList = os.path.split(fileSimPath)
        fileName = tmpSimPathList[-1]
        fileSplit = fileName.replace('.csv', '').split('_')
        if fileSplit[0] == self.name:
            if fileSplit[2] in self.filterDic:
                if fileSplit[1] in self.filterDic[fileSplit[2]]:
                    self.filterDic[fileSplit[2]][fileSplit[1]] = [
                        fileName, tmpSimPath, os.path.abspath(tmpSimPath)]
                else:
                    self.filterDic[fileSplit[2]].update(
                        {fileSplit[1]: [fileName, tmpSimPath, os.path.abspath(tmpSimPath)]})

        # print(fileSplit)

    def __str__(self) -> str:
        return str(self.filterDic)

    def formatPrint(self) -> None:
        'using rich print the dic'
        print(self.name)
        print(self.filterDic)

    def outToFile(self, folderSave: str) -> None:
        'output to file function'
        if os.path.exists(folderSave) == False:  # for input
            os.mkdir(folderSave)

        folderSave = os.path.join(folderSave, self.name)  # add name

        if os.path.exists(folderSave) == False:
            os.mkdir(folderSave)

        PATHTYPE = ['file_Name', 'simple', 'absolute']
        filePath, simPath, absPath = os.path.join(folderSave, PATHTYPE[0]),\
            os.path.join(folderSave, PATHTYPE[1]),\
            os.path.join(folderSave, PATHTYPE[2])

        if os.path.exists(filePath) == False:
            os.mkdir(filePath)

        if os.path.exists(simPath) == False:
            os.mkdir(simPath)

        if os.path.exists(absPath) == False:
            os.mkdir(absPath)

        for typeKey, stateValue in self.filterDic.items():
            fileNameTmp = typeKey+'.txt'
            with open(file=os.path.join(filePath, fileNameTmp), mode='w') as fileFile,\
                open(file=os.path.join(simPath, fileNameTmp), mode='w') as simFile, \
                    open(file=os.path.join(absPath, fileNameTmp), mode='w') as absFile:
                for _, filePathPart in stateValue.items():
                    fileFile.write(filePathPart[0]+'\n')
                    simFile.write(filePathPart[1]+'\n')
                    absFile.write(filePathPart[2]+'\n')


#a = EcgFileFilter('Hello world')
# print(a)
