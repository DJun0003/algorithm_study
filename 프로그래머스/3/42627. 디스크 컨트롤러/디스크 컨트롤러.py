# from collections import deque
# import heapq

# def solution(jobs):
#     answer, len_jobs = 0, len(jobs)
    
#     t = 0
#     wait = []
#     jobs = deque(jobs)
    
#     while True:
#         # 대기열에 넣기    
#         while len(jobs) > 0 and jobs[0][0] <= t:
#             st, cost = jobs.popleft()
#             wait.append([t-st, (st, cost)])
                
#         # 우선순위
#         for j in wait:
#             j[0] = t - j[1][0] + len(wait)*j[1][1]
#         heapq.heapify(wait)
        
#         print(t, wait)
        
#         # 작업
#         if len(wait) == 0:
#             t += 1
#         else:
#             j = heapq.heappop(wait)
#             answer += t - j[1][0] + j[1][1]
#             print(j[1],t - j[1][0] + j[1][1])
#             t += j[1][1]
        
#         if len(wait) == 0  and len(jobs) == 0:
#             break
        
#     print(answer)
#     return answer // len_jobs

from heapq import heappop, heappush
def solution(jobs):
    jobs.sort()
    num = len(jobs)
    waiting = [] # (소요시간, 요청시점)
    count = [] # 각 작업이 몇초 걸렸는지
    now = 0 #현재 시각

    while len(count) != num : 
        while jobs and now >= jobs[0][0] : 
            top = jobs.pop(0)
            heappush(waiting, (top[1], top[0]))

        if jobs and waiting == []:
            top = jobs.pop(0)
            now = top[0]
            heappush(waiting, (top[1], top[0]))
        
        x,y = heappop(waiting)
        now += x 
        count.append(now-y)

    return sum(count)//num

