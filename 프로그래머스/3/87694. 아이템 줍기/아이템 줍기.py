from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    map_ = [[-1]*102 for _ in range(102)]
    
    # 경로 생성
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda l: l*2, r)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x==x1 or x==x2 or y==y1 or y==y2:
                    if map_[x][y] == -1:
                        map_[x][y] = 1
                else:
                    map_[x][y] = 0
                
    cx, cy = characterX*2, characterY*2
    ix, iy = itemX*2, itemY*2
    
    queue = deque([[[cx, cy]]])
    map_[cx][cy] = -1
    while queue:
        cur = queue.popleft()
        q_list = []
        for x, y in cur:
            if x==ix and y==iy:
                return answer // 2 
            if map_[x+1][y] == 1:
                q_list.append([x+1,y])
                map_[x+1][y] = -1
            if map_[x-1][y] == 1:
                q_list.append([x-1,y])
                map_[x-1][y] = -1
            if map_[x][y+1] == 1:
                q_list.append([x,y+1])
                map_[x][y+1] = -1
            if map_[x][y-1] == 1:
                q_list.append([x,y-1])
                map_[x][y-1] = -1
        queue.append(q_list)
        answer +=1
                    
    
    return answer