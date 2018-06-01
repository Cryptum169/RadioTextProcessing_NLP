import re
import os
import jieba
import logging
import gensim
import progressbar
from xml.dom import minidom
from tempfile import mkstemp

newModel = False
try:
    model = gensim.models.Word2Vec.load('data/Model/gensimWord2Vec.bin')
    print('Existing Model Found')
except:
    newModel = True

if newModel:
    print('No existing model found')
    # xmldoc = minidom.parse('data/Corpus/sogou_corpus.data.dat')
    # itemlist = xmldoc.getElementsByTagName('content')

    itemlist = []
    prtPath = os.path.dirname(os.path.abspath(__file__))
    currdir = 'Outputs/Audio2Text'
    allFile = os.listdir(prtPath + '/' + currdir)
    for anyFile in allFile:
        with open(currdir + '/' + anyFile) as fp:
            itemlist.append(fp.read())

    logging.basicConfig(level=logging.INFO)
    resultList = []

    counter = 0.0
    barVal = 0
    with progressbar.ProgressBar(max_value=100) as bar:
        print('Loading and Parsing Text')
        for article in itemlist:
            barVal = counter / len(itemlist) * 100
            # Error Handling
            # try:
            #     val = article.firstChild.nodeValue
            # except:
            #     continue
            val = article

            if not isinstance(val, str):
                continue

            sentenceList = re.split('\。|，|…|', val)

            curr = []
            for sentence in sentenceList:
                curr.append(jieba.lcut(sentence))
            resultList.extend(curr)

            bar.update(barVal)
            counter += 1

    # print(resultList)
    model = gensim.models.Word2Vec(resultList, min_count=1)
    model.save('data/Model/gensimWord2Vec.bin')
    print('Done')

# print('相似度：交通 高架')
# print(model.similarity('交通', '高架'))
# print('交通 车辆')
# print(model.similarity('交通', '车辆'))
# print('高架 车辆')
# print(model.similarity('高架', '车辆'))
# print('事故 道路')
# print(model.similarity('事故', '道路'))
# print('车辆 音乐')
# print(model.similarity('车辆', '音乐'))
