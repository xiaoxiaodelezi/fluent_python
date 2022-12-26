# 用一行就解决了获取和更新单次的出现情况列表，用到了dict.setdefault

import sys
import re

index = {}

WORD_RE = re.compile(r'\w+')
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            #setdefault
            #查找key，不存在的化设定为第二个参数的值，并返回
            #存在已有值
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
