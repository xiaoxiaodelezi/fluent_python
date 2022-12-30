# Bobo知道hello需要person参数，并且从HTTP请求中获取它

import bobo


@bobo.query('/')
def hello(person):
    return 'Hello %s' % person