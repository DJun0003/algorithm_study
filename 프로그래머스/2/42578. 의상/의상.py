from itertools import combinations
from math import prod

def solution(clothes):
    dic = {}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]] += 1
        else:
            dic[c[1]] = 1
    
    answer = 0
    for v in dic.values():
        answer += (v + v*answer)
    return answer