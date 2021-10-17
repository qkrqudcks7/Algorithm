from itertools import combinations

arr = []
sum = 0
for i in range(9):
    a = int(input())
    arr.append(a)
    sum += a
arr.sort()

for i in combinations(arr, 2):
    if sum - i[0] - i[1] == 100:
        arr.remove(i[0])
        arr.remove(i[1])
        break
for i in arr:
    print(i)
