import nlp
import readFile as rf
import json

__transcribe__ = False
__keywordExtract__ = True

def list2str(inlist):
    returnStr = "["
    for item in inlist:
        returnStr += item + ", "
    return returnStr + "]"

allTestCaseDir = rf.retivAllCase()
outputFile = open("Output.txt",'w')
counter = 1
for item in allTestCaseDir:
    testStr = rf.readSingleTestCases(item)

    if __transcribe__:
        name = item.split("/")
        name = name[len(name) - 1]
        transcript = open("Transcript/" + name + ".txt",'w')
        transcript.write(item + "\n")
        transcript.write(testStr)
        transcript.close()

    if __keywordExtract__:
        keyword = nlp.jieba_keyword(testStr)
        outputFile.write(item + "\n")
        outputFile.write(list2str(keyword) + "\n")

    counter += 1
    if counter == int(len(allTestCaseDir) / 10):
        print("10% completed")
    elif counter == int(len(allTestCaseDir) / 4):
        print("25% completed")
    elif counter == int(len(allTestCaseDir) / 2):
        print("50% completed")
    elif counter == int(len(allTestCaseDir) / 4 * 3):
        print("75% completed")

print("Completed")