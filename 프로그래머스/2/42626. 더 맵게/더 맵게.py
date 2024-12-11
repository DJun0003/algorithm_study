import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        f1 = heapq.heappop(scoville)
        if f1>= K:
            return answer
        
        if len(scoville)==0:
            return -1
        
        f2 = heapq.heappop(scoville)
        heapq.heappush(scoville, f1+(f2*2))
        answer += 1
    