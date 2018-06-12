import progressbar
from xml.dom import minidom

xmldoc = minidom.parse('data/Corpus/sogou_corpus.dat')

contentList = xmldoc.getElementsByTagName('content')
titleList = xmldoc.getElementsByTagName('contenttitle')

skipList = []
counter = 0
fileLength = len(contentList)
fileCounter = 0
txtCounter = 0
with progressbar.ProgressBar(max_value=fileLength) as bar:
    outStr = []
    for v in contentList:
        if type(v.firstChild) == type(None):
            content  = ''
            skipList.append(counter)
        # else:
            # content = v.firstChild.nodeValue
            # outStr.append(content)
        counter += 1
        # fileCounter += 1
        bar.update(counter)

        # if (fileCounter == int(fileLength / 10)):
        #     txtCounter += 1
        #     with open('sogou/content' + str(txtCounter) + '.txt','w') as fp:
        #         outStr = '\n'.join(str(v) for v in outStr)
        #         fp.write(outStr)
        #     fileCounter = 0
        #     outStr = []

outStr = []
fileCounter = 0
txtCounter = 0
counter = 0
with progressbar.ProgressBar(max_value=fileLength) as bar:
    for v in titleList:
        if type(v.firstChild) == type(None) or counter in skipList:
            title = ''
        else:
            title = v.firstChild.nodeValue
            outStr.append(title)
        counter += 1
        fileCounter += 1
        bar.update(counter)

        if (fileCounter == int(fileLength / 10)):
            txtCounter += 1
            with open('sogou/title' + str(txtCounter) + '.txt','w') as fp:
                outStr = '\n'.join(str(v) for v in outStr)
                fp.write(outStr)
            fileCounter = 0
            outStr = []