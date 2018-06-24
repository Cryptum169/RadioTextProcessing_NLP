import jieba
import progressbar
from src.Levenshtein import levenshtein_distance
with open('sogou/6.19 - Revised/Content.txt','r') as fp:
    contentLines = fp.readlines()

with open('sogou/6.19 - Revised/Title.txt','r') as fp:
    titleLines = fp.readlines()

errorLog = []
with progressbar.ProgressBar(max_value=len(titleLines) * 3) as bar:
    j = 0
    contentSegList = []
    for x in contentLines:
        k = jieba.lcut(x)
        contentSegList.append(k)
        j += 1
        bar.update(j)

    titleSegList = []
    for x in titleLines:
        k = jieba.lcut(x)
        titleSegList.append(k)
        j += 1
        bar.update(j)

    for i in range(len(titleLines)):
        if len(contentSegList[i]) > levenshtein_distance(contentSegList[i], titleSegList[i]) + 2:
            errStr = "Error suspected: Content is \n{}Title is \n{}".format(contentLines[i], titleLines[i])
            errorLog.append(errStr)
        j += 1
        bar.update(j)

with open('result.txt','w') as fp:
    fp.write(''.join(errorLog))


# counter = 0
# contentSkiplist = []
# for x in contentLines:
#     if len(x) < 200:
#         contentSkiplist.append(counter)
#     counter += 1

# titleSkipList = []
# counter = 0
# for y in titleLines:
#     if len(y) < 10:
#         titleSkipList.append(counter)
#     counter += 1

# combinedList = list(set(contentSkiplist + titleSkipList))
# combinedList = sorted(combinedList, reverse=True)

# for index in combinedList:
#     del contentLines[index]
#     del titleLines[index]

# with open('sogou/6.19 - Revised/Content.txt','w') as fp:
#     fp.write(''.join(contentLines))

# with open('sogou/6.19 - Revised/Title.txt','w') as fp:
#     fp.write(''.join(titleLines))

