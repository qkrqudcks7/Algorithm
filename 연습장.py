import heapq

food=[3,1,2]
q=[]
for i in range(len(food)):
   heapq.heappush(q,(food[i],i+1))

print(q)
print(heapq.heappop(q)[0])