'''
 Process Sogou News corpus into 20 txt files of Q and A
 Q as Content, A as title
 file 1 to 10 as content1.txt to content10.txt, similar nomenclature for title.txt
'''
__restart__ = False
if __restart__:
    path = 'Outputs/Revised_Corpus'
else:
    path = 'sogou/test'

# import jieba
import progressbar
total_dataset_num = 0
with progressbar.ProgressBar(max_value=10) as bar:
    for i in range(1,11):
        content_skipList = []
        contentLines = []
        title_skipList = []
        titleLines = []
        with open(path + '/content' + str(i) + '.txt', 'r') as fp:
            contentLines = [line[:-1] for line in fp]
            counter = 0
            last = ['”', '。', '＂', '！','？']
            for content in contentLines:

                if __restart__:
                    if len(content) > 600 or len(content) < 200:
                        content_skipList.append(counter)
                        counter += 1
                        continue
                    
                    if content[-1:] not in last:
                        lastindex = max(content.rfind(x) for x in last)
                        if lastindex < 5:
                            content_skipList.append(counter)
                            counter += 1
                            continue
                        content = content[:lastindex + 1]
                        
                    detailedContent = ['［详细］', '［　详细　］',
                                    '【详细】', '点击阅读详细内容', '点击进入']
                    if any(x in content for x in detailedContent):
                        content_skipList.append(counter)
                        counter += 1
                        continue

                    if content.find('．．．') != -1:
                        content_skipList.append(counter)
                        counter += 1
                        continue
                    
                    if content.count('：') > 3:
                        content_skipList.append(counter)
                        counter += 1
                        continue

                    contentLines[counter] = content.replace(
                        '（来源：南方都市报南都网）', '')

                    punc = ['，', '：']
                    # Strip Initials
                    skip = False
                    hongkongJournal = ['记者', '报道', '实习']
                    report = ['电','讯','消息','报道']
                    deleteTitle = content[:25]
                    newspaper = content[:15]
                    journalWord = max(deleteTitle.find(word) for word in hongkongJournal)

                    leftPa = deleteTitle.find('（')
                    rightPa = deleteTitle.find('）')
                    if leftPa != rightPa != -1 and (leftPa < journalWord < rightPa or rightPa - leftPa > 2):
                        if any(x in content[rightPa + 1] for x in punc):
                            rightPa += 1
                        content = content[rightPa + 1:]
                        skip = True

                    newsWord = max(newspaper.find(word) for word in report)
                    if newsWord != -1 and not skip:
                        try:
                            report.index(deleteTitle[newsWord])
                            place = 1
                        except:
                            place = 2
                        if any(x in content[newsWord + place] for x in punc):
                            place += 1
                        if rightPa != -1:
                            content = content[rightPa + place + 1:]
                        else:
                            content = content[newsWord + place:]

                    if deleteTitle.find('】') != -1:
                        content = content[deleteTitle.find('】') + 1:]

                    count = 0
                    for character in content:
                        if character < u'\u4e00' or character > u'\u9fff':
                            count += 1

                    if count/len(content) > 0.2:
                        content_skipList.append(counter)
                        counter += 1
                        continue

                    content = content.replace('视频－', '')
                    content = content.replace(u'\u3000', '')
                    content = content.replace('视频：', '')
                    content = content.replace('视屏：', '')  # ¯\_(ツ)_/¯
                    contentLines[counter] = content

                    contentLines[counter] = content.replace(u'\ue40c', '')

                counter += 1

        with open(path + '/title' + str(i) + '.txt', 'r') as fp:
            titleLines = [line[:-1] for line in fp]
            counter = 0

            for content in titleLines:
                if __restart__:
                    if len(content) > 600 or len(content) < 12:
                        title_skipList.append(counter)
                        counter += 1
                        continue

                    count = 0
                    for character in content:
                        if character == '！' or character == '【':
                            title_skipList.append(counter)
                            break
                        if character < u'\u4e00' or character > u'\u9fff':
                            count += 1

                    if count / len(content) > 0.2:
                        title_skipList.append(counter)
                        counter += 1
                        continue

                    leftPaIndex = max(content.rfind(k)
                                      for k in ['（', '【', '［'])
                    if leftPaIndex != -1 and leftPaIndex > len(content) - 8:
                        content = content[:leftPaIndex]

                    rightPaIndex = max(content.rfind(k)
                                       for k in ['）', '】', '］'])
                    if rightPaIndex != -1 and rightPaIndex < len(content) - 5:
                        content = content[rightPaIndex + 1:]

                    content = content.replace('视频－','')
                    content = content.replace('视频：','')
                    content = content.replace('视屏：','') # ¯\_(ツ)_/¯
                    content = content.replace('主题：','') # ¯\_(ツ)_/¯
                    titleLines[counter] = content

                counter += 1

        combinedList = list(set(content_skipList + title_skipList))
        combinedList = sorted(combinedList, reverse=True)

        # print(combinedList)

        for index in combinedList:
            del contentLines[index]
            del titleLines[index]

        print('Data Set {} has {} content lines and {} title lines'.format(str(i), str(len(contentLines)), str(len(titleLines))))
        if len(contentLines) != len(titleLines):
            raise Exception('Unequal number of content and title lines')
        else:
            total_dataset_num += len(contentLines)

        with open('sogou/test/content' + str(i) + '.txt', 'w') as fp:
            fp.write('\n'.join(contentLines))

        with open('sogou/test/title' + str(i) + '.txt', 'w') as fp:
            fp.write('\n'.join(titleLines))

        bar.update(i)

print('Total of {} data sets'.format(str(total_dataset_num)))

