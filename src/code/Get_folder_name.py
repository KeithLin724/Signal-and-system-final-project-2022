from pprint import pprint
import os

folderTree = ['CW', 'HT']
dataFolder = 'src\data'


folderFileName = dict()
for nameFolder in folderTree:
    name = os.path.join(os.path.abspath(dataFolder), nameFolder)

    try:
        folderFileName.update({nameFolder: os.listdir(name)})

    except Exception as e:
        print(e)
        exit()

pprint(folderFileName)

# make a folder name
absFolderPath = os.path.join(os.path.abspath('src'), 'name of folder')
if os.path.exists(absFolderPath) == False:
    os.mkdir(absFolderPath)

for key, listOfFileName in folderFileName.items():

    fileNameTmp = os.path.join(absFolderPath, ''.join([key, 'Folder', '.txt']))

    with open(fileNameTmp, mode='w') as f:
        for i in listOfFileName:
            f.write(i+'\n')

# make a abs file path in file
PathOfFolderPath = os.path.join(os.path.abspath('src'), 'name absfolder')
if os.path.exists(PathOfFolderPath) == False:
    os.mkdir(PathOfFolderPath)


listSaveAbsPath = dict()
for nameFolder in folderTree:
    for root, directories, files in os.walk(os.path.join(os.path.abspath(dataFolder), nameFolder)):
        tmp = [os.path.join(root, name) for name in files]
        listSaveAbsPath.update({nameFolder: tmp})

pprint(listSaveAbsPath)
for key, listOfFilePath in listSaveAbsPath.items():

    fileNameTmp = os.path.join(PathOfFolderPath, ''.join(
        [key, 'Folder abs Path', '.txt']))

    with open(fileNameTmp, mode='w') as f:
        for i in listOfFilePath:
            f.write(i+'\n')
