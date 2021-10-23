def solution(n):
    answer = 0
    b = [[0,0,0] for i in range(1001)]
    print(b)
    b[1] = [3, 5, 7]
    b[2] = [13, 15, 17]
    b[3] = [27, 29, 31]

    count = 18

    for i in range(4, n + 1):
        x = b[n-1][0]+count
        y = b[n-1][0]+count
        z = b[n-1][0]+count
        b[i][0] = x
        b[i][1] = y
        b[i][2] = z
        count += 4

    return sum(b[n])

print(solution(5))