# 배경=Lock크기 +(key크기-1)*2
# key를 (0,0)부터 (key크기+lock크기-1)까지 반복
# 이 때 key와 lock을 더해주는데 1이면 true
# 성립할 때까지 진행하며 end까지도 성립하지 않으면 key를 90도 돌려서 다시 시전
# key가 360도 돌아갈 때까지 true가 있으면 출력

def rotate(key):
    return list(zip(*key[::-1]))


def insert(key, lock, start_i, start_j, end):
    length = len(lock) + 2 * (len(key) - 1)
    background = [[0 for i in range(length)] for j in range(length)]

    # key를 먼저 background에 넣는다
    for i in range(len(key)):
        for j in range(len(key)):
            background[start_i + i][start_j + j] = key[i][j]

    # 그리고 lock을 key가 넣어진 background에 더해준다
    for i in range(len(key) - 1, end):
        for j in range(len(key) - 1, end):
            background[i][j] += lock[i - len(key) + 1][j - len(key) + 1]
            if background[i][j] != 1:
                return False
    return True


def solution(key, lock):
    end = len(key) + len(lock) - 1

    for k in range(4):
        for i in range(end):
            for j in range(end):
                start_i = i
                start_j = j
                if insert(key, lock, start_i, start_j, end):
                    return True
        key = rotate(key)
    return False
