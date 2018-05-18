fw1 = open("中文停用词表(1208个).txt",'r')
fw2 = open('停用词表.txt','r')

sw1 = list(fw1.read().splitlines())
sw2 = list(fw2.read().splitlines())
end = sw1 + list(set(sw2) - set(sw1))

swl = open("stopWordLib.txt",'w')
for item in end:
    swl.write("%s\n" % item)