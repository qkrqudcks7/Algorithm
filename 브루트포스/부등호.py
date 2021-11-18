n = int(input())
sign = input().split()
check = [False] * 10
mx = ""
mn = ""

def possible(i,j,k):
    if k=="<":
        return i<j
    if k ==">":
        return i>j

def solve(count,temp):
    global mn,mx
    if count==n+1:
        if not len(mn):
            mn = temp
        else:
            mx = temp
        return

    for i in range(10):
        if not check[i]:
            if count == 0 or possible(temp[-1],str(i),sign[count-1]):
                check[i] = True
                solve(count+1, temp + str(i))
                check[i] = False

solve(0,"")