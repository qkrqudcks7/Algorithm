from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))


def countByRange(array, leftV, rightV):
    right_index = bisect_right(array, rightV)
    left_index = bisect_left(array, leftV)
    return right_index - left_index


count = countByRange(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)
