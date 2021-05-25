import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식시간,음식번호)
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간

    length = len(food_times)  # 남은 음식의 개수

    # 먹기위해 사용한 시간 +(현재의 음식시간-이전 음식시간)*남은 음식의 개수
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식은 제외
        previous = now  # 이전 음식 시간 재설정

    # 음식 번호 기준으로 정렬
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]
