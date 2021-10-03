import heapq

n = int(input())
array = []

for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(array, (abs(x), x))
    else:
        try:
            print(heapq.heappop(array)[1])
        except:
            print(0)
