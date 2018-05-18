import json
import os

def getTestDirectory():
    prtPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testPath = prtPath + "/Test_Data"
    return testPath

def getTestNames():
    return getTestDirectory() + "/readFile.json"
    # modify later to read all file names

def readSingleTestCases(testFile):
    with open(testFile) as json_data:
        testData = json.load(json_data)

    returnString = ''
    for item in testData:
        returnString += item['text']
    
    return returnString
    
def retivAllCase():
    pass
    return None