#2.1
symbols = '%^*)'
codes1 = []
for symbol in symbols:
    codes1.append(ord(symbol))
print(codes1)

#2.2
codes2 = [ord(symbol) for symbol in symbols]
print(codes2)

codes3 = [ord(symbol) for symbol in symbols if ord(symbol) > 40]
print(codes3)

#2.3
beyond_ascii = list(filter(lambda c: c > 40, map(ord, symbols)))
print(beyond_ascii)

#2.4
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

#2.5
print(ord(symbol) for symbol in symbols)
print(tuple(ord(symbol) for symbol in symbols))
import array

print(array.array('I', (ord(symbol) for symbol in symbols)))

#2.6
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

#2.12
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

#2.17
import bisect

haystack = [1, 4, 5, 6, 8, 9]
needle = 0
position = bisect.bisect(haystack, needle)
print(position)