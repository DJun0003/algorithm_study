from collections import deque

move = [[-1,0], [1,0], [0,-1], [0, 1]]

def bfs(maps):
    q = deque([[0,0,1]])
    maps[0][0] = 0
    
    while q:
        cur_y, cur_x, count = q.popleft()
        if cur_y==len(maps)-1 and cur_x == len(maps[0])-1:
            return count
        
        for m in move:
            ny, nx = cur_y+m[0], cur_x+m[1]
            if ny>-1 and ny<len(maps) and nx>-1 and nx<len(maps[0]):
                if maps[ny][nx] == 1:
                    q.append([ny, nx, count+1])
                    maps[ny][nx] = 0
        
    return -1
        
    
def solution(maps):
    return bfs(maps)