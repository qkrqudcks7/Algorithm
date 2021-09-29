n = int(input())

for i in range(n):
    a = input()
    left = 0
    for j in a:
        if j == '(':
            left += 1
        else:
            left -= 1
        if left<0:
            print("NO")
            break
    if left == 0:
        print("YES")
    elif left>0:
        print("NO")
