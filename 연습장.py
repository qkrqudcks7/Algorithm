def solution(n):
    answer = 0
    temp=0
    for i in range(1,n+1):
        temp+=i
        for j in range(i+1,n+1):
            if temp==n:
                answer+=1
                temp=0
                break
            else:
                temp+=j 
    return answer
print(solution(15))