import heapq

def solution(scv, K):
    ans = 0
    heapq.heapify(scv)
    
    while len(scv) > 1:
        first = heapq.heappop(scv)
        
        if first >= K:
            return ans
        
        second = heapq.heappop(scv)
        new = first + (2 * second)
        ans += 1
        
        heapq.heappush(scv, new)
    
    first = heapq.heappop(scv)
    if first < K:
        return -1
    else:
        return ans