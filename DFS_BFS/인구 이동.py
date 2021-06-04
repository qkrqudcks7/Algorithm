n,l,r=map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

result=0
