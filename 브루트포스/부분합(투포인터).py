# 투포인터 문제입니다 암기하세요!

n, s = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = 0
minL = 1e9
temp = 0

while start < n:
    if temp >= s:
        minL = min(minL, end - start)
        temp -= a[start]
        start += 1

    elif end == n:
        break
    else:
        temp += a[end]
        end += 1

if minL == 1e9:
    print(0)
else:
    print(minL)
