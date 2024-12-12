from collections import deque

def can_change(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            diff += 1
        if diff > 1:
            return False
    return True

def solution(begin, target, words):
    answer = 0

    if not target in words:
        return 0
    
    q = deque([[begin]])
    visited = [False] * len(words)
    
    while q:
        cur_list = q.popleft()
        next_list = []
        
        answer += 1
        for w in cur_list:
            for i in range(len(words)):
                if not visited[i] and can_change(w, words[i]):
                    if words[i] == target:
                        return answer
                    
                    visited[i] = True
                    next_list.append(words[i])
        q.append(next_list)
    return 0