N = int(input())
nines = [int('9' + '0' * i) for i in range(0, len(str(N)))]  # if 120 --> [9, 90, 900]
result = 0

for i, s in enumerate(nines):
    if s == nines[-1]:  # 마지막 자릿수를 계산할 때
        result += len(str(s)) * (N - sum(nines[:-1]))  # result += 3 * 21
    else:
        i += 1
        result += i * s

print(result)
