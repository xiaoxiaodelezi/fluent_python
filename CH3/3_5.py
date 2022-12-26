# 利用defaultdic实例而不是setdefault方法
# 创建一个从单次到其出现情况的映射

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

#collections.defaultdict
#表达式dd['key']，如果不存在key，会调用函数list来创建一个新的value，返回这个表的引用
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            #index[word]，如果word不存在
            # 1.调用list函数创建一个列表
            # 2.index中生成word作为key，list作为value的键值对
            # 3.index[word]返回value
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
