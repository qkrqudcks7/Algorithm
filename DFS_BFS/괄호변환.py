#  균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0  # 왼쪽 괄호의 수
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


# 올바른 괄호 문자인지 판단
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            # 쌍이 맞지 않으면 False 반환
            if count == 0:
                return False
            # 나중에 빼줘야 됨
            count -= 1

    return True


def solution(p):
    answer = ""
    if p == "":
        return answer

    index = balanced_index(p)

    u = p[:index + 1]
    v = p[index + 1:]

    # "올바른 괄호 문자열이면" v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        #  첫번째 문자와 마지막 문자를 제거
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
