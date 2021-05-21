s = input()
zero_count = 0
one_count = 0

if s[0] == "0":
    zero_count += 1
else:
    one_count += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '0':
            zero_count += 1
        else:
            one_count += 1

print(min(zero_count,one_count))
