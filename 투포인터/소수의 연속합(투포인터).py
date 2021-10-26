N = int(input())

a = [False, False] + [True] * (N - 1)
prime_num = []

for i in range(2, N + 1):
    if a[i]:
        prime_num.append(i)
        for j in range(2 * i, N + 1, i):
            a[j] = False

answer = 0
start = 0
end = 1
temp = prime_num[start]

while start < len(prime_num):
    if temp == N:
        answer += 1
        temp -= prime_num[start]
        start += 1

    if end == len(prime_num) and temp < N:
        break

    elif temp < N:
        temp += prime_num[end]
        end += 1
    elif temp > N:
        temp -= prime_num[start]
        start += 1

print(answer)
