import json
import src.readFile as rf

alltestCaseDir = rf.retivAllCase()
outputDir = 'Outputs/'

for anyFile in alltestCaseDir:
    transcript = rf.readSingleTestCases(anyFile)
    fileName = anyFile.split('/')[-1:]
    fp = open(outputDir + fileName[0],'w')
    fp.write(transcript)
    fp.close()

