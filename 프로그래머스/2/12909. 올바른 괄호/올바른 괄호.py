from collections import deque

def solution(string):
    left = deque([])
    
    for s in string:
        if s == '(':
            left.append(s)
        else:
            if len(left) == 0:
                return False
            else:
                left.pop()
        
        
    return len(left) == 0