n = int(input())

count = 0
room = []
for i in range(n):
    a, b = map(int, input().split())
    room.append((a, b))
room = sorted(room, key=lambda i: (i[1], i[0]))

temp = []
temp.append(room[0])
room.pop(0)

for i in room:
    a, b = i
    if temp[-1][1] <= a:
        temp.append((a, b))
        continue
print(len(temp))
