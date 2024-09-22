from collections import deque

def solution(begin, target, words):    
    queue = deque([[begin, 0]])
    l = len(begin)
    visits = [False] * len(words)
    if target not in words:
        return 0
    
    while queue:
        cur, ans = queue.popleft()
        
        if cur == target:
            return ans
        
        for i in range(len(words)):
            if not visits[i]:
                diff = 0
                for j in range(l):
                    if cur[j] != words[i][j]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    queue.append([words[i], ans+1])
                    visits[i] = True
    
    return 0
            