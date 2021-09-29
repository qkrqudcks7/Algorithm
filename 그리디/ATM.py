n = int(input())
s = list(map(int, input().split()))
s.sort()
sum = 0
temp = 0
for i in s:
    temp += i
    sum += temp
print(sum)
