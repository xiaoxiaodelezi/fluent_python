# 把partial应用到tag函数上

from functools import partial


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


print(tag)

picture = partial(tag, 'img', cls='pic-fram')
print(picture(src='wumpus.jpeg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)