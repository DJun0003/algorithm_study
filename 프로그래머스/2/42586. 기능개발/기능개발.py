from math import ceil

def solution(progresses, speeds):
    answer = []
    num, t = 1, ceil((100-progresses[0]) / speeds[0])
    for i in range(1, len(progresses)):
        time = ceil((100-progresses[i]) / speeds[i])
        if t < time:
            answer.append(num)
            num, t = 1, time
        else:
            num += 1
    if num > 0:
        answer.append(num)
        
    return answer
