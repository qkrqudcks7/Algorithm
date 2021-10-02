from bisect import bisect_left

n = int(input())
array = list(map(int, input().split()))

list = []
num = 0

for i in array:
    if not list:
        list.append(i)
        num += 1
        continue
    if list[-1] < i:
        list.append(i)
        num += 1
    else:
        index = bisect_left(list, num)
        list[index] = num
print(num)
