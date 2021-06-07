import heapq

n = int(input())

heap = []

for i in range(n):
    heapq.heappush(heap, int(input()))
result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sumV = one + two
    result += sumV
    heapq.heappush(heap, sumV)

print(result)
