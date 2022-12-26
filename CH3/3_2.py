#这段程序从索引中获取单词出现的频率信息，并把它们写进对应的列表里
""" 创建一个从单词到其出现情况的映射"""

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    #enumerate(迭代对象，起始index)
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            #match.group
            word = match.group()
            #match.start
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
for word in sorted(index, key=str.upper):
    print(word, index[word])
