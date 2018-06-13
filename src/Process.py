'''
 Process Sogou News corpus into 20 txt files of Q and A
 Q as Content, A as title
 file 1 to 10 as content1.txt to content10.txt, similar nomenclature for title.txt
'''
import progressbar
total_dataset_num = 0
with progressbar.ProgressBar(max_value=10) as bar:
    for i in range(1,11):
        content_skipList = []
        contentLines = []
        title_skipList = []
        titleLines = []
        with open('Outputs/Revised_Corpus/content' + str(i) + '.txt','r') as fp:
            contentLines = [line[:-1] for line in fp]
            counter = 0
            for content in contentLines:
                if len(content) > 600 or len(content) < 100:
                    content_skipList.append(counter)
                    counter += 1
                    continue
                
                count = 0
                for character in content:
                    if character < u'\u4e00' or character > u'\u9fff':
                        count += 1

                if count/len(content) > 0.2:
                    content_skipList.append(counter)
                    counter += 1
                    continue

                counter += 1

        with open('Outputs/Revised_Corpus/title' + str(i) + '.txt', 'r') as fp:
            titleLines = [line[:-1] for line in fp]
            counter = 0

            for content in titleLines:
                if len(content) > 600 or len(content) < 12:
                    title_skipList.append(counter)

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

