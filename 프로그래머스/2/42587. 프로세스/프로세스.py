from collections import deque
import heapq

def solution(priors, location):
    sorted_prior = sorted(priors, reverse=True)
    sorted_prior = deque(sorted_prior)
    pro_loc = deque([(priors[i], i) for i in range(len(priors))])
    count = 0
    
    while len(pro_loc) > 0:
        p, l = pro_loc.popleft()
        
        if p < sorted_prior[0]:
            pro_loc.append((p,l))
        else:
            sorted_prior.popleft()
            count += 1
        
            if l == location:
                break
            
        
    
    return count