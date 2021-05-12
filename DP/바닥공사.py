n = int(input())

t = [0] * 1001

t[1] = 1
t[2] = 3

for i in range(3, n + 1):
    t[i] = (t[i - 1] + 2 * t[i - 2]) % 796796

print(t[n])
