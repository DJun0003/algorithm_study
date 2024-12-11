from collections import deque

def solution(numbers, target):
    cur_list = [0]
    numbers = deque(numbers)
    
    for num in numbers:
        new_list = []
        for cur in cur_list:
            new_list.append(cur+num)
            new_list.append(cur-num)
        cur_list = new_list
    
    return cur_list.count(target)