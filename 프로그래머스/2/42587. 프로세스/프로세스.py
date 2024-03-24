from collections import deque
import heapq

def solution(priors, location):
    queue = deque([(priors[i], i) for i in range(len(priors))])
    count = 0
    
    while True:
        p, l = queue.popleft()
        
        if any (p < q[0] for q in queue):
            queue.append((p,l))
        else:
            count += 1
            if l == location:
                break
            
        
    
    return count