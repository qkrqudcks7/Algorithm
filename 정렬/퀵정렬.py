# 퀵정렬의 평균 시간 복잡도는 O(NlogN)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    # 피벗은 첫번째
    pivot = array[0]
    # 피벗을 제외한 리스트
    tail = array[1:]

    left_side = [i for i in tail if i <= pivot]  # 분할된 왼쪽 부분
    right_side = [i for i in tail if i > pivot]  # 분할된 오른쪽 부분

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))