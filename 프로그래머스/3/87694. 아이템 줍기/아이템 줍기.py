def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    l = []
    
    # 경로 생성
    for x1,y1,x2,y2 in rectangle:
        while len(l) < x1+1:
            l.append([100, 0])
        
        ymin, ymax = l[x1]
        if y1 < ymin:
            l[x1][0] = y1
        if y2 > ymax:
            l[x1][1] = y2
        
    print(l)
            
    
    return answer