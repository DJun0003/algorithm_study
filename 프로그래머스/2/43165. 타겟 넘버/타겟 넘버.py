from collections import deque

def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    
    answer = sum(map(lambda x: x == target, leaves))
    
    return answer