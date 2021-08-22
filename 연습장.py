def solution(grades):
    answer = []
    grade = {"A+": 1, "A0": 2, "A-": 3, "B+": 4, "B0": 5, "B-": 6, "C+": 7, "C0": 8, "C-": 9, "D+": 10, "D0": 11,
             "D-": 12, "F": 13}
    result = {}

    for i in grades:
        x, y = i.split()
        point = grade.get(y)
        if x in result:
            if point < grade.get(result[x]):
                result.pop(x)
                result[x] = y
        else:
            result[x] = y

    print(result)

    l = sorted(result.items(), key=lambda x : grade.items())
    print(l)
    for i in l:
        temp = ""
        temp += i[0]
        temp += " "
        temp += i[1]

        answer.append(temp)
    return answer


print(solution(["DS7651 A0", "CA0055 D+", "AI5543 C0", "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-", "AI5543 D+", "DS7651 A+", "OS1808 B-"]))