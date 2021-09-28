# 최장 공통 부분 수열

one = input()
two = input()

len1 = len(one)
len2 = len(two)

board = [[0] * (len2 + 1) for i in range(len1 + 1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if one[i-1] == two[j-1]:
            # 길이는 (두 글자가 추가되기 전 가장 큰 길이 + 1)이 됨
            board[i][j] = board[i-1][j-1]+1
        else:
            # 기존에 주어진 문자열로 만들 수 있던 최대 길이를 갖게 됨
            board[i][j] = max(board[i-1][j], board[i][j-1])
print(board[-1][-1])
