# Algorithm
## :key: 복잡도

### :bulb: 시간 복잡도 : 얼마나 오래 걸리는지
1. O(1) 상수 시간 ex) 연산이 한번만 수행되는 상수연산
2. O(logN) 로그 시간 ex) 
3. O(N) 선형 시간 ex) N에 비례하는 연산 , 반복문
4. O(NlogN) 로그 선형 시간
5. O(N^2) 이차 시간 ex) N x N 2중 반복문
6. O(N^3) 삼차 시간 ex) 3중
7. O(2^n) 지수 시간

- 연산 횟수가 10억을 넘어가면 c기준 1초
### :bulb: 공간 복잡도 : 얼마나 많은 메모리를 차지 하는지
1. int a[1000] = 4KB
2. int a[1000000]=4MB
3. int a[2000][2000]=16MB

- 파이썬 기준 1초에 2000만번 수행함

## :pushpin: 그리디(탐욕법)

### :bulb: 가장 좋아 보이는 것만을 선택해서 문제를 풀 수 있는가?
( ex '가장 큰 순서대로' , '가장 작은 순서대로' )


## :pushpin: 구현

### :bulb: 완전탐색 : 모든 경우의 수를 다 계산
- 데이터가 100만개 이하일 때 사용하면 적절함
### :bulb: 시뮬레이션 : 알고리즘을 한 단계씩 차례대로


## :pushpin: DFS/BFS

### :bulb: DFS(Depth-First-Search) : 깊이 우선 탐색
- 노드와 간선으로 이루어진 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조에 기초한다

### :bulb: BFS(Breadth-First-Search) : 너비 우선 탐색
- 노드와 간선으로 이루어진 그래프에서 가까운 노드부터 탐색하는 알고리즘
- 큐 자료구조를 이용한다
- 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어 가까운 노드부터 탐색을 진행하게 된다.


## :pushpin: 정렬

### :bulb: 선택정렬 : '매번 가장 작은 것을 선택한다'는 의미의 원시적 알고리즘
### :bulb: 삽입정렬 : 각 데이터를 확인하여 적절한 위치에 삽입하는 알고리즘
- 삽입 정렬은 두 번째 데이터부터 시작한다
- 데이터가 거의 정렬되어 있을 때 훨씬 효율적이다.
- O(N^2)의 시간 복잡도를 가진다

### :bulb: 퀵정렬 : 기준 데이터를 설정, 그 기준 큰 데이터와 작은 데이터를 바꾸는 알고리즘
- 피벗이라는 기준이 사용 된다.
- 리스트의 첫번째 데이터가 피벗이 된다.
- 리스트의 왼쪽부터 피벗보다 큰 데이터를 찾고, 오른쪽부터 피벗보다 작은 데이터를 찾는다
- O(NlogN)의 시간 복잡도를 가진다

### :bulb: 계수정렬 : 특정 조건이 부합할 때만 사용할 수 있는 알고리즘. 매우 빠르다
- 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용할 수 있다.
- 데이터 크기 차이가 100만이 넘지 않을때 효과적이다.
- 모든 범위를 담을 수 있는 리스트를 선언해야 한다.
- O(N+K)의 공간복잡도를 가진다.


## :pushpin: 이진 탐색
- 배열 내부의 데이터가 정렬되어야만 사용 가능하다.
- 시작점, 끝점, 중간점의 변수를 사용하여 중간점에 위치한 데이터를 반복적으로 비교한다.

## :pushpin: 다이나믹 프로그래밍
- 큰 문제를 작은 문제로 나눌 수 있을 때
- 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일할 때
### :bulb: Top-Down방식(메모제이션) : 큰 문제를 해결하기 위해 작은 문제를 호출 ( 하향식 )
### :bulb: Bottom-Up : 작은 문제부터 차근차근 답을 도출하는 방법 ( 상향식 )

- 재귀를 쓰는 Top-Down 방식은 시스템상 재귀 함수의 스택 크기가 한정되어 있을 수 있으니, 되도록 Bottom-Up 방식으로 해보자

< 그래프 구현 방법 >

ex) 노드개수: V , 간선개수: E
### :bulb: 인접 리스트 방식: 리스트를 이용하는 방식
- 간선의 개수 만큼인 O(E) 만큼의 메모리 공간 필요
- 다익스트라 알고리즘
### :bulb: 인접 행렬 방식 2차원 배열을 이용하는 방식
- O(V^2) 만큼의 메모리 공간 필요
- 플로이드 워셜 알고리즘

## :pushpin: 최단 경로

### :bulb: 다익스트라 최단 경로
- 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
- 매번 '가장 비용이 적은 노드'를 선택하는 과정을 반복하기 때문에 그리디 알고리즘으로 분류됨
- '각 노드에 대한 현재까지의 최단 거리' 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신한다.
- 
- <b>우선순위 큐를 사용하자</b>

1. 출발노드를 설정한다
2. 최단 거리 테이블을 초기화한다
3. 방문하지 않은 노드 중에서 최단 거리가 짧은 노드를 선택한다
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다 ( 그리디 알고리즘 )
5. 3번과 4번을 반복한다

### :bulb: 플로이드 워셜 최단 경로
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 구할 때
- O(N^3) 시간 복잡도를 가진다
- 2차원 리스트에 '최단 거리' 정보를 저장한다
- 다이나믹 프로그래밍 알고리즘을 가진다



## :pushpin: 그래프 이론

