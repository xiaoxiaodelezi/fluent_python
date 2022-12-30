# 提取函数的签名

from inspect import signature


def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


sig = signature(clip)
#命令行执行
#sig # doctest: +ELLIPSIS
print(sig)

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
