knight = input()
row = int(knight[1])
column = int(ord(knight[0])) - int(ord('a')) + 1

step = [(-2, -1), (-1, -2), (1, -2), (2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1)]
result = 0
for i in step:
    nextRow = row + i[0]
    nextColumn = column + i[1]

    if 1 <= nextRow <= 8 and 1 <= nextColumn <= 8:
        result += 1

print(result)