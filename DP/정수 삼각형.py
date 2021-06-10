n=int(input())
dp=[]

for i in range(n):
    dp.append(list(map(int,input().split())))

# 둘째 줄 부터 내려가면서 확인
for i in range(1,n):
    for j in range(i+1):
        if j==0:

