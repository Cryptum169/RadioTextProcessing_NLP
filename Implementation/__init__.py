import readFile
import jieba
import jieba.analyse

# 抽取广播文本
testStr = readFile.readSingleTestCases(readFile.getTestNames())

# 关键词 - 词频
punctuation = "！？。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞"
segList = jieba.cut_for_search(testStr)
occList = dict()

## 统计词频
for word in segList:
    if word not in punctuation:
        if word not in occList:
            occList[word] = 1
        else:
            occList[word] += 1

## 整理list
newList = dict()
for kv in sorted(occList.items(), key = lambda kv: (-kv[1], kv[0])):
    newList[str(kv[0])] = kv[1]

print(list(newList.keys())[:50])

# 关键词 - NLP(?) 抽取
tdidf = jieba.analyse.extract_tags(testStr, 20, False, ('n','ns'))
txtRank = jieba.analyse.textrank(testStr, 20, False, ('n','ns'))

## 统计交集
print(sorted(list(set(tdidf) & set(txtRank))))
