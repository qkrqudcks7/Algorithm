n = int(input())
array = list(map(int, input().split()))
reserve_array = array[::-1]

d_front =[1] * n
d_rear = [1] * n

for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            d_front[i] = max(d_front[i], d_front[j]+1)
        if reserve_array[j] < reserve_array[i]:
            d_rear[i] = max(d_rear[i],d_rear[j]+1)

result = [0]*n
for i in range(n):
    result[i] = d_front[i] + d_rear[n-1-i]-1

print(max(result))
