import heapq

def solution(jobs):
    jobs.sort(key = lambda x: (x[0], x[1]), reverse=True)
    waits = []
    cur = 0
    ans = 0
    num = len(jobs)
    
    while len(waits) or len(jobs):
        while len(jobs) and jobs[-1][0] <= cur:
            j = jobs.pop()
            heapq.heappush(waits, [j[1], j[0]])
        
        if not len(waits):
            j = jobs.pop()
            heapq.heappush(waits, [j[1], j[0]])
            cur = j[0]
        
        w = heapq.heappop(waits)
        cur += w[0]
        ans += cur - w[1]
    
    return ans // num
    
    