# 본체는 정렬시켜줘야 됨
n = int(input())
s1 = list(map(int, input().split()))
s1.sort()

m = int(input())
s2 = list(map(int, input().split()))

def binary(l, s1, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if l == s1[mid]:
        return 1
    elif l < s1[mid]:
        return binary(l, s1, start, mid - 1)
    else:
        return binary(l, s1, mid + 1, end)


for i in s2:
    start = 0
    end = len(s1) - 1
    print(binary(i, s1, start, end))
