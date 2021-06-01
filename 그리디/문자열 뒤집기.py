s = input()
zero_count = 0
one_count = 0

if s[0] == "0":
    zero_count += 1
else:
    one_count += 1

for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        if s[i] == '0':
            zero_count += 1
        else:
            one_count += 1

print(min(zero_count, one_count))
