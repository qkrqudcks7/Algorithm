n,c= map(int,input().split())
a=[]

for i in range(n):
    a.append(int(input()))

a.sort()

start=1
end=a[-1]-a[0]
result=0

while(start<=end):
