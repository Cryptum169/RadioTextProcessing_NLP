import json
import os

def getTestDirectory():
    prtPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testPath = prtPath + '/Sample_Data'
    return testPath

def getTestNames():
    return getTestDirectory() + '/readFile.txt'
    # modify later to read all file names

def readSingleTestCases(testFile):
    with open(testFile) as json_data:
        testData = json.load(json_data)

    returnString = ""
    for item in testData:
        try:
            returnString += item['text']
        except:
            returnString += item['statement']
    
    return returnString
    
def retivAllCase():
    path = getTestDirectory()
    astuff = os.listdir(path)
    finalList = list(str())
    for item in astuff:
        item = path + "/" + item
        finalList.extend(racRecurHelper(item))
    return finalList

def racRecurHelper(name):
    returnList = list()
    if os.path.isdir(name):
        pass
        # This DFS block will cause json to complain about double quote and single quote
        # , yet to figure out why, commented out for now
        # for item in os.listdir(name):
        #     item = name + "/" + item
        #     returnList.extend(racRecurHelper(item))
    else:
        if name[-4:] == ".txt":
            returnList.append(name)
    return returnList

        