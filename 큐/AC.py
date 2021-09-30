t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    if n == 0:
        print("error")
    else:
        s = input()
        s= s[1:-1]
        s = list(map(int,s.split(",")))
        check = False
        for j in p:
            if j == "R":
                s = s[::-1]
            elif j == "D":
                if len(s) == 0:
                    print("error")
                    check = True
                    break
                else:
                    s.pop(0)
        if not check:
            print(s)
