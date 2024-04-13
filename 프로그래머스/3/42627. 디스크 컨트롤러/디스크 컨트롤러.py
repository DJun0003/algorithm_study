from collections import deque
from heapq import heappush, heappop

def solution(jobs):
    answer, len_jobs = 0, len(jobs)
    jobs.sort()
    
    t = 0
    wait = []
    jobs = deque(jobs)
    
    while jobs or wait:
        # 대기열에 넣기    
        while jobs and jobs[0][0] <= t:
            st, cost = jobs.popleft()
            heappush(wait, [cost, st])
        
        if jobs and not wait:
            st, cost = jobs.popleft()
            heappush(wait, [cost, st])
            t = st
        
        # 작업
        cost, st = heappop(wait)
        t += cost
        answer += t - st
        
        # print(t, t-st, (st, cost))
    return answer // len_jobs

# def solution(jobs):
#     jobs.sort()
#     num = len(jobs)
#     waiting = [] # (소요시간, 요청시점)
#     count = [] # 각 작업이 몇초 걸렸는지
#     now = 0 #현재 시각

#     while len(count) != num : 
#         while jobs and now >= jobs[0][0] : 
#             top = jobs.pop(0)
#             heappush(waiting, (top[1], top[0]))

#         if jobs and waiting == []:
#             top = jobs.pop(0)
#             now = top[0]
#             heappush(waiting, (top[1], top[0]))
        
#         x,y = heappop(waiting)
#         now += x 
#         count.append(now-y)

#     return sum(count)//num

