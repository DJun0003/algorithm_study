from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    nodes = deque([[begin, 0]])
    v = [False] * len(words)
    while nodes:
        n, depth = nodes.popleft()
        if n == target:
            return depth
        
        for i, w in enumerate(words):
            if not v[i]:
                # cnt = 0
                # for ii in range(len(n)):
                #     if n[ii] != w[ii]:
                #         cnt += 1
                # if cnt == 1:
                #     nodes.append([w, depth+1])
                #     v[i] = True
                #     # words.remove(w)
                
                for ii in range(len(n)-1):
                    if n[:ii]+n[ii+1:] == w[:ii]+w[ii+1:]:
                        nodes.append([w, depth+1])
                        v[i] = True
                if n[:-1] == w[:-1]:
                    nodes.append([w, depth+1])
                    v[i] = True
    return 0

# solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])