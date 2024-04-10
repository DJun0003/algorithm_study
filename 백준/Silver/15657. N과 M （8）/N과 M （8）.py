import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
answer = []

def solution():
    if len(answer) == m:
        print(*answer)
        return
    
    for i in range(n):
        if not answer or (nums[i] >= answer[-1]):
            answer.append(nums[i])
            solution()
            answer.pop()
    return 

solution()