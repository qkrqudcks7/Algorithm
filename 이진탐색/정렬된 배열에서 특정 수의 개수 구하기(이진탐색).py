# x의 첫 번째 위치 구하기
def binary_search_start(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            # 해당 값을 가지는 원소중에서 가장 왼쪽에 있는 경우만 인덱스 반환
            if mid - 1 < 0 or array[mid - 1] != target:
                return mid
            else:
                end = mid - 1
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# x의 마지막 위치 구하기
def binary_search_end(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            if mid + 1 >= len(array) or array[mid + 1] != target:
                return mid
            else:
                start = mid + 1
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


N, x = map(int, input().split())
array = list(map(int, input().split()))

if binary_search_start(array, x, 0, len(array) - 1) == -1:
    print(-1)
else:
    print(binary_search_end(array, x, 0, len(array) - 1) - binary_search_start(array, x, 0, len(array) - 1) + 1)
