import heapq

# 왼쪽 힙은 최대 힙으로 정렬하고, 오른쪽 힙은 최소 힙으로 정렬하면
# 왼쪽 힙의 첫번째 요소는 항상 중앙값이 된다.
n = int(input())
left = []
right = []

for i in range(n):
    x = int(input())

    # 왼쪽과 오른쪽 원소의 길이가 같으면 왼쪽에 새 값을 저장
    if len(left) == len(right):
        heapq.heappush(left, (-x, x))
    else:
        heapq.heappush(right, (x, x))

    # 만약 오른쪽 heap보다 왼쪽이 더 크면 오른쪽 왼쪽을 바꿔준다.
    if right and left[0][1] > right[0][1]:
        leftV = heapq.heappop(left)[1]
        rightV = heapq.heappop(right)[1]
        heapq.heappush(right, (leftV, leftV))
        heapq.heappush(left, (-rightV, rightV))
    print(left[0][1])
