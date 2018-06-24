# Merge separated content and title .txt files 
# into single content.txt and title.txt files
contentLines = []
for i in range(1,11):
    with open('sogou/6.19 - Revised/title' + str(i) + '.txt','r') as fp:
        contentLines.extend(fp.readlines())

result = ''.join(contentLines)
with open('sogou/6.19 - Revised/Title.txt','w') as fp:
    fp.write(result)

contentLines = []
for i in range(1,11):
    with open('sogou/6.19 - Revised/content' + str(i) + '.txt','r') as fp:
        contentLines.extend(fp.readlines())

result = ''.join(contentLines)
with open('sogou/6.19 - Revised/Content.txt','w') as fp:
    fp.write(result)