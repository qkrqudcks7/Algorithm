import math

print("{}      {}      {}      {}".format("n", "파이", "수열계산", "오차"))
print("----------------------------------------------------")
temp = 1
for i in range(1000, 10001, 1000):
    pi = round(math.pi, 6)
    for j in range(2, i + 1):
        temp += (1 / j ** 2)

    diff = round(math.sqrt(6 * temp), 6)
    result = round(pi - diff, 6)
    print("{}  {}  {}  {}".format(i, pi, diff, result))
    temp = 1
