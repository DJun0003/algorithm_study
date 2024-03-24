from collections import deque

def solution(string):
    left = []
    
    for s in string:
        if s == '(':
            left.append(s)
        else:
            try:
                left.pop()
            except:
                return False
    

    return len(left) == 0