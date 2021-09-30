t = int(input())  # 테스트케이스 수
for i in range(0, t):

    # n과 m을 입력받는다. - 문서 개수와 순서
    n, m = list(map(int, input().split(' ')))

    # 큐에 원소 입력
    q = list(map(int, input().split(' ')))

    # 큐의 각 원소에 인덱스 부여하기 위해서 enumerate 사용 2,1,3,4-> (2,0),(1,1),(3,2),(4,3)
    q = [(i, idx) for idx, i in enumerate(q)]

    count = 0
    while True:
        # 큐에서의 원소 순서가 최대 중요도와 같은 경우
        if q[0][0] == max(q, key=lambda x: x[0])[0]:
            count += 1
            # 문서의 찾고자하는 위치 m과 인덱스 번호가 같으면 출력
            if q[0][1] == m:
                print(count)
                break
            else:
                # m과 같지 않다면 원소를 빼서
                q.pop(0)
        # 맨뒤에 삽입한다.
        else:
            q.append(q.pop(0))