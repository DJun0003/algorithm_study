from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    move = [[-1,0], [0,1], [1,0], [0,-1]]
    queue = deque([[0, 0, 1]])
    maps[0][0] = 0
    
    while queue:
                
        cn, cm, ans = queue.popleft()
        if cn == n-1 and cm == m-1:
            return ans
        
        for dir in move:
            new_n, new_m = min(max(0, cn + dir[0]), n-1), min(max(0, cm + dir[1]), m-1)
            if maps[new_n][new_m] == 1:
                queue.append([new_n, new_m, ans+1])
                maps[new_n][new_m] = 0
    return -1