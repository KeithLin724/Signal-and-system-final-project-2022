import pandas as pd


def Cal_HR(inputList: list) -> list:
    reHR = []
    inputListSize = len(inputList)
    for index, val in enumerate(inputList):
        if index < inputListSize:
            tranHRPart = 60*200/(inputListSize[index+1]-val)
            reHR.append(tranHRPart)
