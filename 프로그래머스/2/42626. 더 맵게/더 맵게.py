import heapq
from collections import deque

def solution(scv, K):
    ans = 0
    heapq.heapify(scv)
    while True:
        f1 = heapq.heappop(scv)
        
        if f1 < K:
            try:
                heapq.heappush(scv, f1+(heapq.heappop(scv)*2))
                ans += 1
            except:
                return -1
        else:
            break
    return ans