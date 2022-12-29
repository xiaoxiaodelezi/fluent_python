# 使用lambda表达式反转拼写，然后依次给单次列表排序

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits, key=lambda word: word[::-1]))
