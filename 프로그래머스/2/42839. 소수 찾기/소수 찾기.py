from itertools import permutations
from math import sqrt

def is_prime(num):
    if num == 0 or num == 1:
        return False
    sq = sqrt(num)
    is_ = True
    if type(sq) != int:
        for i in range(2, int(sq)+1):
            if num % i == 0:
                is_ = False
    return is_
        

def solution(numbers):
    ans_list = []
    for i in range(1,len(numbers)+1):
        for n in list(permutations(numbers, i)):
            num = int(''.join(n))
            if num in ans_list:
                continue
            elif is_prime(num):
                ans_list.append(num)
    return len(ans_list)
            
            
        
        
    
    