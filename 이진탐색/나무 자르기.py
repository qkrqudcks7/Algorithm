n, m = map(int, input().split())
wood = list(map(int, input().split()))

start = 0
end = max(wood) - 1


def binary(wood, m, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    temp = 0
    for i in wood:
        if (i - mid) > 0:
            temp += i - mid

    if temp == m:
        return mid
    elif temp > m:
        return binary(wood, m, mid + 1, end)
    else:
        return binary(wood, m, start, mid - 1)


print(binary(wood, m, start, end))
