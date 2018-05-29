import json
import os

def getTestDirectory():
    prtPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testPath = prtPath + '/Implementation/asr-result/baiduasr-result'
    # change to aliasr-result when processing Aliyun data 
    return testPath

# Depreciated
def getTestNames():
    return getTestDirectory() + '/readFile.txt'
    # modify later to read all file names

def readSingleTestCases(testFile):
    with open(testFile) as json_data:
        try:
            testData = json.load(json_data)
        except:
            # This try block deals with incorrect json format that has ' instead of "
            data = json_data.read().replace("'",'"')
            try:
                testData = json.loads(data)
                # This try block deals with empty transcript file
            except:
                return ""

    returnString = ""
    for item in testData:
        try:
            returnString += item['text']
        except:
            returnString += item['statement']
    
    return returnString

# Return list of all file
def retivAllCase():
    path = getTestDirectory()
    astuff = os.listdir(path)
    finalList = list(str())
    for item in astuff:
        item = path + "/" + item
        finalList.extend(racRecurHelper(item))
    return finalList

# DFS Directory Search Helper
def racRecurHelper(name):
    returnList = list()
    if os.path.isdir(name):
        for item in os.listdir(name):
            item = name + "/" + item
            returnList.extend(racRecurHelper(item))
    else:
        if name[-4:] == ".txt":
            returnList.append(name)
    return returnList

        