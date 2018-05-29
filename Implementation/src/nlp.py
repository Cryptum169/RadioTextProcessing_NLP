import jieba
import jieba.analyse
from pyhanlp import HanLP

def jieba_keyword(instr):
    # TDIDF
    tdidf = jieba.analyse.extract_tags(instr, 20, False)
    # TextRank
    txtRank = jieba.analyse.textrank(instr, 20, False)
    return sorted(list(set(tdidf) & set(txtRank)))

def jieba_occurence(instr):
    swFile = open("Stop_Word_Lib/stopWordLib.txt",'r')
    stopWord = list(swFile.read().splitlines())
    punctuation = "！？。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀"\
    "｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞"
    segList = jieba.cut_for_search(instr)
    occList = dict()
    ## 统计词频
    for word in segList:
        if word not in punctuation and word not in stopWord:
            if word not in occList:
                occList[word] = 1
            else:
                occList[word] += 1
    ## 整理list
    newList = dict()
    for kv in sorted(occList.items(), key = lambda kv: (-kv[1], kv[0])):
        newList[instr(kv[0])] = kv[1]

    return list(newList.keys())[:10]


def hanlp_keyword(instr):
    # Text Rank
    return HanLP.extractKeyword(instr, 10)