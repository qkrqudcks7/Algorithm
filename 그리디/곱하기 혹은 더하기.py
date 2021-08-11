s = input()
count = int(s[0])
for i in range(1, len(s)):
    if count == 0:
        count += int(s[i])
    else:
        count *= int(s[i])

print(count)
