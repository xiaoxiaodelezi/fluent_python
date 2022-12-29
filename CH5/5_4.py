# 根据反向拼写给一个单词列表排序

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


def reverse(word):
    return word[::-1]


print(reverse('testing'))

print(sorted(fruits, key=reverse))
