import os
import jieba
import logging
import pandas as pd

logging.basicConfig(level = logging.INFO)
df = pd.read_csv('Outputs/csv_Output/Output.csv', encoding='gb18030')

summaryList = list(df['description'])
contentList = list(df['Transcript'])

logging.basicConfig(level=logging.INFO)
length = len(summaryList)
seg_sum_list = []
for summary in summaryList:
    seg_str = ','.join(jieba.lcut(str(summary)))
    seg_sum_list.append(seg_str)

seg_cont_list = []
for content in contentList:
    seg_str = ','.join(jieba.lcut(str(content)))
    seg_cont_list.append(seg_str)

fileCounter = 1
lineCounter = 0
for i in range(0,len(summaryList)):
    if ('fp' not in locals() or fp.closed):
        fp = open('Outputs/Training_Set/Summary/' + str(fileCounter) + '.txt','w')
        lineCounter = 0

    fp.write(seg_sum_list[i] + '\n')
    lineCounter += 1

    if (lineCounter > int(len(summaryList) / 5)):
        lineCounter = 0
        fileCounter += 1
        fp.close()

fileCounter = 1
lineCounter = 0
for i in range(0,len(contentList)):
    if ('fpc' not in locals() or fpc.closed):
        fpc = open('Outputs/Training_Set/Transcript/' + str(fileCounter) + '.txt','w')
        lineCounter = 0

    fpc.write(seg_cont_list[i] + '\n')
    lineCounter += 1

    if (lineCounter > int(len(seg_cont_list) / 5)):
        lineCounter = 0
        fileCounter += 1
        fpc.close()
