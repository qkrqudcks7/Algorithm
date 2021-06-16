from collections import deque
import copy

v=int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph =[[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time =[0]*(v+1)

# 방향 그래프의 모든 간선 입력
for i in range(1,v+1):
    data = list(map(int,input().split()))
    # 첫번째는 시간 정보를 담고 있으므로 time에 저장
    time[i]=data[0]
    for j in data[1:-1]:
        indegree[i]+=1
        graph[j].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q=deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now=q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            result[i] = max(result[i],result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in range(1,v+1):
        print(result[i])
topology_sort()

