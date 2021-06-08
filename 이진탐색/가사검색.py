from bisect import bisect_left, bisect_right

array = [[] for i in range(10001)]
reversed_array = [[] for i in range(10001)]


def countByRange(a, leftV, rightV):
    right_index = bisect_right(a, rightV)
    left_index = bisect_left(a, leftV)

    return right_index - left_index


def solution(words, queries):
    answer = []

    for i in words:
        array[len(i)].append(i)
        reversed_array[len(i)].append(i[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for i in queries:
        if i[0] != "?":
            res = countByRange(array[len(i)], i.replace('?', 'a'), i.replace('?', 'z'))
        else:
            res = countByRange(reversed_array[len(i)], i[::-1].replace('?', 'a'), i[::-1].replace('?', 'z'))
        answer.append(res)
    return answer
