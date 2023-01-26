# 使用asyncio和aiohttp包实现异步下载脚本

import asyncio
import aiohttp

import time
import sys
import os

BASE_URL = 'https://www.fluentpython.com/data/flags'

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


@asyncio.coroutine
def get_flag(cc):
    url = ''
