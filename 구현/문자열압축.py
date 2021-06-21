def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    # 1개 단위부터
    for i in range(1, len(s) / 2 + 1):
        count = 1
        tempStr = s[0:i]

        for j in range(i, len(s), i):
            if s[j:j + i] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[j:j + i]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    return min(length)
