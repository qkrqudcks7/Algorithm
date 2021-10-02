n = int(input())
s1 = list(map(int, input().split()))

m = int(input())
s2 = list(map(int, input().split()))

dict = {}

for i in s1:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(' '.join(str(dict[m]) if m in dict else '0' for m in s2))
