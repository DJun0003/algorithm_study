import math

def solution(progresses, speeds):
    answer = []
    bf_time = 0
    ans = 0
    for i in range(len(progresses)):
        time = math.ceil((100-progresses[i])/speeds[i])
        if time > bf_time:
            bf_time = time
            if ans != 0:
                answer.append(ans)
            ans = 1
        else:
            ans += 1
    
    answer.append(ans)
    
    return answer