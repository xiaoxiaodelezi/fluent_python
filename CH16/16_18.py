#简单的伪代码

_i = iter(EXPR)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = e.value
else:
    while 1:
        _s = yield _y
        try:
            _y = _.send(s)
        except StopIteration as _e:
            _r = e.value
            break

RESULT = _r
