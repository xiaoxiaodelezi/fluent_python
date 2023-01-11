# 用于原地重写文件的上下文管理器

import csv

with inplace(csvfilenmae, 'r', newline='') as (infh, outfh):
    reader = csv.reader(infh)
    writer = csv.writer(outfh)

    for row in reader:
        row += ['new', 'columns']
        writer.writerow(row)
