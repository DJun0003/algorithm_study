from collections import deque

def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    adds = deque([0])

    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
        l = len(adds)
        for i in range(l):
            a = adds.popleft()
            adds.append(a+num)
            adds.append(a-num)
    

    answer = sum(map(lambda x: x == target, leaves))
    return adds.count(target)