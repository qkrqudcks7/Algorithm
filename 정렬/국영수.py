n = int(input())

array = []

for i in range(n):
    name, kor, math, eng = input().split()
    array.append((name, int(kor), int(math), int(eng)))

new_array = sorted(array, key=lambda i: (-int(i[1]), int(i[2]), int(i[3]), i[0]))

for i in new_array:
    print(i[0])
