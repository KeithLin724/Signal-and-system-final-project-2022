'''
Title:Get folder name
Written By KYLiN
This is a get folder name code,output is a file path in .txt file
Date: 18/5/2022
'''

from pprint import pprint
import os

folderTree = ['CW', 'HT']
dataFolder = 'src\\data'

folderFileName = dict()
for nameFolder in folderTree:
    name = os.path.join(os.path.abspath(dataFolder), nameFolder)

    try:
        folderFileName.update({nameFolder: os.listdir(name)})

    except Exception as e:
        print(e)
        exit()

pprint(folderFileName)

tmpSaveFolder = os.path.join(os.path.abspath('src'), 'FileTxt')
if not os.path.exists(tmpSaveFolder):
    os.mkdir(tmpSaveFolder)

# make a folder name
absFolderPath = os.path.join(tmpSaveFolder, 'name of folder')
if not os.path.exists(absFolderPath):
    os.mkdir(absFolderPath)

for key, listOfFileName in folderFileName.items():

    fileNameTmp = os.path.join(absFolderPath, ''.join([key, 'Folder', '.txt']))

    with open(fileNameTmp, mode='w') as f:
        f.write('\n'.join(listOfFileName))

# make a abs file path in file
PathOfFolderPath = os.path.join(tmpSaveFolder, 'name absfolder')
if not os.path.exists(PathOfFolderPath):
    os.mkdir(PathOfFolderPath)

listSaveAbsPath = dict()
for nameFolder in folderTree:
    for root, directories, files in os.walk(
            os.path.join(os.path.abspath(dataFolder), nameFolder)):

        tmp = [os.path.join(root, name) for name in files]
        listSaveAbsPath.update({nameFolder: tmp})

pprint(listSaveAbsPath)
for key, listOfFilePath in listSaveAbsPath.items():

    fileNameTmp = os.path.join(PathOfFolderPath,
                               ''.join([key, 'Folder abs Path', '.txt']))

    with open(fileNameTmp, mode='w') as f:
        f.write('\n'.join(listOfFilePath))
