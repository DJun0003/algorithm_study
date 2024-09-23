from collections import deque

def solution(rectangle, chx, chy, itx, ity):
    maps = [[-1] * 102 for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if y==y1 or y==y2 or x==x1 or x==x2:
                    if maps[y][x] == -1:
                        maps[y][x] = 1
                else:
                    maps[y][x] = 0
    
    chy, chx = chy*2, chx*2
    ity, itx = ity*2, itx*2
    q = deque([[chy, chx, 0]])
    maps[chy][chx] = -1
    
    while q:
        cury, curx, ans = q.popleft()
        if cury==ity and curx==itx:
            return ans
        
        for my, mx in [[1,0], [-1,0], [0,1], [0,-1]]:
            ny, newy, nx, newx = cury+my, cury+(2*my), curx+mx, curx+(2*mx)
            if newy<2 or newy>100 or newx<2 or newx>100:
                continue
            if maps[newy][newx]==1 and maps[ny][nx]==1:
                q.append([newy, newx, ans+1])
                maps[newy][newx] = -1
            
                    