n = int(input())
s = list(map(int, input().split()))
temp = []
for i in range(len(s)):
    check = False
    for j in range(i, len(s)):
        if i < j:
            temp.append(str(j))
            check = True
            break
    if not check:
        temp.append(str(-1))

print(" ".join(temp))
