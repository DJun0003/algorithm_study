from collections import deque

def solution(numbers, target):
    
    q = deque([0])
    
    for num in numbers:
        new_q = deque([])
        while q:
            cur = q.popleft()
            new_q.append(cur+num)
            new_q.append(cur-num)
        q = new_q
    
    return q.count(target)