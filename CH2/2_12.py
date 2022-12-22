# 一个包含3个列表的列表，嵌套的3个列表各自有3个元素
# 模仿一个井字游戏

board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'

print(board)