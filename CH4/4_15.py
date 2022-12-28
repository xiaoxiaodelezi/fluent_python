# 4_14中函数的实例

import unicodedata
import string

def shave_marks(txt):
    norm_txt=unicodedata.normalize('NFD',txt)
    shaved=''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC',shaved)

order = 'café'
print(shave_marks(order))