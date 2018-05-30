import os
import re
import pandas as pd
import numpy as np

def matchSummary2Content():
    # Load in list of file
    prtPath = os.path.dirname(os.path.abspath(__file__))
    optFilePath = prtPath + '/Outputs'
    transcriptList = os.listdir(optFilePath)
    # 20170515-10023-66104.m3u8_channel_0.txt

    fileID = []
    for fileName in transcriptList:
        if 'm3u8_channel_0' in fileName:
            fileID.append(re.split('\.',fileName)[0])
        else:
            fileID.append(re.split('\.|_',fileName)[0])

    # ['20170515-10023-66104', '20170422-74629-62948', ... , 'nRFX43yr8S']

    df = pd.read_csv('filter_content.csv')
    nameSeries = df['\m3u8_url']
    # http://short-audio.ajmide.com/audio/201805/22/EZjE5F8Ebb1526976158203

    contentList = ['N/A'] * len(nameSeries)
    nameList = list(nameSeries)

    notFoundCounter = 0
    for csvEntry in nameList:
        name = ''.join(str(csvEntry).split('/')[-1:])
        if '.' in name:
            # Some url exists as .file
            name = ''.join(re.split('\.',name)[0])

        if name in fileID:
            with open('Outputs/' + transcriptList[fileID.index(name)]) as fp:
                index = nameList.index(csvEntry)
                contentList[index] = fp.read()
        else:
            notFoundCounter += 1

    df['Transcript'] = pd.Series(contentList)
    # df.to_csv('Output.csv')
    print('{} existing csv entry not found'.format(notFoundCounter))

    # Filter out too short Entries
    for eachContent in contentList:
        if len(str(eachContent)) < 50:
            index = contentList.index(eachContent)
            df.drop(df.index[index])
        
    df.to_csv('Output.csv',encoding='gb18030')


if __name__ == '__main__':
    print('Please check directory path, there could be changes unaccounted for')
    matchSummary2Content()