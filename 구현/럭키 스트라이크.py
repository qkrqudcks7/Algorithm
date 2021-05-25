n = int(input())
changeN = str(n)

first = 0
second = 0

for i in range(0, len(changeN) // 2):
    first += int(changeN[i])

for i in range(len(changeN) // 2, len(changeN)):
    second += int(changeN[i])

if first == second:
    print("LUCKY")
else:
    print("READY")
