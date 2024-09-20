from itertools import permutations
from math import sqrt

def solution(numbers):
    num_list = []
    for n in range(1, len(numbers)+1):
        num_list += list(map(lambda x: int(''.join(x)), permutations(numbers, n)))
    
    ans = []
    for num in set(num_list):
        if num==0 or num==1:
            continue

        is_p = True
        for i in range(2, int(sqrt(num))+1):
            if num%i == 0:
                is_p = False
                break
        if is_p:
            ans.append(num)
    
    return len(ans)
            
            