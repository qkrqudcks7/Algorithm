from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    # 투입할 친구의 최소값을 찾아야 하므로 len(dist)+1로 초기화
    answer = len(dist) + 1

    #  0부터 length-1 까지의 위치를 각 시작점으로 설정
    for i in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for j in list(permutations(dist, len(dist))):
            count = 1  # 투입할 친구의 수
            #  해당 친구가 점검할 수 있는 마지막 위치
            position = weak[i] + j[count-1]