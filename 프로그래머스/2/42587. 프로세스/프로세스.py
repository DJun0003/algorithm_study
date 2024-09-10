from collections import deque

def solution(priorities, location):
    total = len(priorities)
    priorities = deque(priorities)
    loc = deque([i for i in range(total)])
    
    while loc:
        p, l = priorities.popleft(), loc.popleft()
        if loc and p < max(priorities):
            priorities.append(p)
            loc.append(l)
        elif l == location:
            return total - len(loc)
    
    return total
            