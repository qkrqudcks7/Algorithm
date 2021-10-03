import heapq

n = int(input())
array = []
for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(array, x)
    else:
        try:
            print(heapq.heappop(array))
        except:
            print(0)
