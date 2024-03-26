from collections import deque
def solution(maps):
    n, m = len(maps)-1, len(maps[0])-1
    queue = deque([[0,0,1]])
    maps[0][0] = 0
    
    while queue:
        place = queue.popleft()
        
        for move in ([1,0], [0,1], [-1,0], [0,-1]):
            new_y, new_x = place[0] + move[0], place[1] + move[1]
            if new_y < 0 or new_y > n or new_x < 0 or new_x > m:
                continue
            if new_y == n and new_x == m:
                return place[2]+1
            if maps[new_y][new_x]:
                maps[new_y][new_x] = 0
                queue.append([new_y, new_x, place[2]+1])
                
    
    
    return -1