import jieba
import logging
import gensim
import progressbar
import re
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
    xmldoc = minidom.parse('data/Corpus/sogou_corpus.data.dat')
    itemlist = xmldoc.getElementsByTagName('content')
    logging.basicConfig(level=logging.INFO)
    resultList = []
    
    counter = 0.0
    barVal = 0
    with progressbar.ProgressBar(max_value=100) as bar:
        for article in itemlist:
            barVal = counter / len(itemlist) * 100
            # Error Handling
            try:
                val = article.firstChild.nodeValue
            except:
                continue

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