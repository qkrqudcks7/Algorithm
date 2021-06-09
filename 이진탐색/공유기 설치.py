n,c=map(int,input().split())

array=[]
for i in range(n):
    array.append(int(input()))

array.sort()

start=1
end = array[-1]-array[0]
result=0

while(start<=end):
    mid = (start+end)//2
    value=array[0]
    count=1

    for i in range(1,n):
