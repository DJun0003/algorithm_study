import heapq
from collections import deque

def solution(jobs):
    num = len(jobs)
    jobs = deque(sorted(list(map(lambda x: [x[1], x[0]], jobs)), key=lambda x:x[1]))
    pq = []
    time = jobs[0][1]
    answer = 0
    
    while True:
        while jobs and time>=jobs[0][1]:
            heapq.heappush(pq,jobs.popleft())
        if len(pq)==0:
            if jobs:
                time = jobs[0][1]    
            else:
                break
            
        else:
            cur = heapq.heappop(pq)
            time += cur[0]
            answer += (time-cur[1])
            
    
    return answer // num