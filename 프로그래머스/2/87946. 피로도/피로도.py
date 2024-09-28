from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for seq in permutations(dungeons):
        k_ = k
        ans = 0
        for min_, lost_ in seq:
            if k_ >= min_:
                ans += 1
                k_ -= lost_
        if ans > answer:
            answer = ans
    return answer