# -*- coding: utf-8 -*-
import re
import jieba
import math
import operator
import src.Levenshtein as lt

def returnString():
    with open('data/Test_Cases/2.txt','r') as fp:
        temp = [line[:-1] for line in fp]
    return ''.join(temp)

def getConnection(sentence, article, model):
    # Sentence as segmented word lists, article as segmented sentence list
    returnList = []
    for i in range(len(article)):
        compare = jieba.lcut(article[i])
        if lt.levenshtein_distance(compare, sentence) + 5 < min(len(sentence), len(compare)) or lt.sentence_similarity(compare,sentence,model) > 0.3:
            returnList.append(i)
    return returnList


def score(sentence, article, scoreMap, connectedVertice, damping = 0.85, model = None):
    # Article as list of sentence
    # Sentence as whole sentence
    score = 0
    sent_seg = jieba.lcut(sentence)
    wij = 0
    for index in connectedVertice[sentence]:
        sent = article[index]
        if sent != sentence:
            seg_list = jieba.lcut(sent)
            wij += lt.similarity(sent_seg, seg_list, model = model) * scoreMap[sent]
    score = (1 - damping) + damping * wij
    return score

def intmain(article = None):
    article = returnString()
    vecModel = lt.load_model()
    article = re.split('。|，|\n', article)
    scoreMap = dict()
    connectionMap = dict()
    for sentence in article:
        scoreMap[sentence] = 1
        sent_seg = jieba.lcut(sentence)
        connectionMap[sentence] = getConnection(sent_seg, article, vecModel)

    # print(scoreMap)
    print('Article length of {} sentences'.format(len(article)))

    prevDiff = 0
    for i in range(100):
        scoreDiff = 0
        for sentence in article:
            newScore = score(sentence = sentence, article = article, scoreMap = scoreMap, connectedVertice = connectionMap, model = vecModel)
            scoreDiff += abs(newScore - scoreMap[sentence])
            scoreMap[sentence] = newScore
        print('Epoch: {}, diff: {}'.format(i, scoreDiff))
        if abs(prevDiff - scoreDiff) < 0.000001:
            break
        else:
            prevDiff = scoreDiff
    temp = sorted(scoreMap.items(), key=operator.itemgetter(1), reverse = True)[:10]
    print(temp)

if __name__ == "__main__":
    intmain()