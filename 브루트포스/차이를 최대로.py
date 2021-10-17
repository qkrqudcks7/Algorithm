from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
result = 0
for i in permutations(arr, n):
    i = list(i)
    temp = 0
    for j in range(len(i) - 1):
        temp += abs(i[j] - i[j + 1])

    if result < temp:
        result = temp
print(result)
