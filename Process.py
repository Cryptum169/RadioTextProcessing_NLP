import progressbar

with progressbar.ProgressBar(max_value=10) as bar:
    for i in range(1,11):
        content_skipList = []
        contentLines = []
        with open('sogou/content' + str(i) + '.txt','r') as fp:
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

        title_skipList = []
        titleLines = []
        with open('sogou/title' + str(i) + '.txt', 'r') as fp:
            titleLines = [line[:-1] for line in fp]
            counter = 0
            for content in titleLines:
                count = 0
                for character in content:
                    if character < u'\u4e00' and character > u'\u9fff':
                        count += 1

                if count/len(content) > 0.2:
                    title_skipList.append(counter)
                    counter += 1
                    continue
                counter += 1

        combinedList = list(set(content_skipList + title_skipList))
        combinedList = sorted(combinedList, reverse=True)

        # print(combinedList)
        # print(len(titleLines))
        # print(len(contentLines))

        for index in combinedList:
            del contentLines[index]
            del titleLines[index]

        with open('sogou/test/content' + str(i) + '.txt', 'w') as fp:
            fp.write('\n'.join(contentLines))

        with open('sogou/test/title' + str(i) + '.txt', 'w') as fp:
            fp.write('\n'.join(titleLines))

        bar.update(i)

