from collections import deque

a=[1,2,3,4,5]

q=deque(a)
q.popleft()
q.append(6)
print(q)