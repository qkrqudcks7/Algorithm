s = input()
a = []
for i in range(0, len(s)):
    a.append(int(s[i]))
result = 0
for i in range(0, len(a)):
    if result <= 1:
        result += a[i]
    else:
        result *= a[i]

print(result)
