

from file_data_class import FileDataClass  # import the File Date
import matplotlib.pyplot as plt  # about plot the graph
import os  # read file in lib
from pprint import pprint
import pandas as pd


pathLoc = 'src\FilterOutput'
name = ['CW']
filePathType = 'simple'
# test cw
hrPathList = []
indexPathList = []
svPathList = []

locCheck = os.path.join(pathLoc, name[0], filePathType)
listOfFileName = None
if os.path.isdir(locCheck):
    listOfFileName = os.listdir(locCheck)
    pprint(listOfFileName)
testCheck = os.path.join(locCheck, listOfFileName[2])

dataPath = []
with open(file=testCheck, mode='r') as f:
    dataPath = f.readlines()

dataPath = [i.replace('\n', '') for i in dataPath]

pprint(dataPath)

fileDate = FileDataClass(dataPath[0])

#fileDate = FileDataClass(testCheck)
thing = fileDate.get_file_data()
thingName = fileDate.get_file_path()
pprint(thingName)
'''
b = [int(thing.name)]
b[1:] = thing
thing = pd.Series(b)
'''
# list(thing.values)
pprint(thing)
fileDate.save_to_png(folderPath='tmp')
#thing.plot(legend=True,  label=thing.name)
#saveFileName = thing.name.replace(' ', '_')
#saveFileName = f'tmp\{saveFileName}.png'
# pprint(f'tmp\{saveFileName}.png')
# plt.savefig(saveFileName)
# plt.show()
