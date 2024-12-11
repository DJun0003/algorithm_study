from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    total_p = len(priorities)
    max_p = max(priorities)
    while True:
        cur_p = priorities.popleft()
        if cur_p < max_p:
            priorities.append(cur_p)
            location = (location-1+len(priorities)) % len(priorities)
        else:
            if location == 0:
                return total_p - len(priorities)
            else:
                location -= 1
                max_p = max(priorities)
    
        