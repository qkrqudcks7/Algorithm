n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)


def binary_search(array, start, end, target):
    if start > end:
        return None
    total = 0
    mid = (start + end) // 2

    for i in array:
        if (i - mid) > 0:
            total += i - mid
    if total == target:
        return mid
    elif total > target:
        return binary_search(array, mid + 1, end, target)
    else:
        return binary_search(array, start, mid - 1, target)


print(binary_search(array, start, end, m))
