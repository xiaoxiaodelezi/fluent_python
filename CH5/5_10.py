# tag函数用于生成HTML标签，使用名为cls的关键字参数传入“class”属性
# 这是一种变通方法，因为“class”是Python的关键字


def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name)
                         for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
