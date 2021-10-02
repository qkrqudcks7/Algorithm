n, c = map(int, input().split())
list = []

for i in range(n):
    list.append(int(input()))

list.sort()

start = 1
end = list[-1] - list[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = list[0]
    count = 1

    for i in range(1, n):
        if list[i] >= value + mid:
            value = list[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
