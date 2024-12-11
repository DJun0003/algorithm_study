from collections import deque

def solution(begin, target, words):
    
    if not target in words:
        return 0
    
    q = deque([[begin]])
    visited = [False] * len(words)
    count = 0
    
    while q:
        cur_list = q.popleft()
        new_list = []
        for cur in cur_list:
            if cur==target:
                return count
            
            for i in range(len(words)):
                if not visited[i] and sum(map(lambda x: words[i][x]!=cur[x], range(len(cur))))==1:
                    new_list.append(words[i])
                    visited[i] = True
        count += 1
        q.append(new_list)
    
    return count