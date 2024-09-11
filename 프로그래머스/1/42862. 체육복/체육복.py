def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    same = lost & reserve
    lost = sorted(list(lost - same))
    reserve = sorted(list(reserve - same))
    
    r, l = 0, 0
    students = 0
    
    for l in range(len(lost)):
        while r<len(reserve) and reserve[r] < lost[l]-1:
            r += 1
        
        if r >= len(reserve):
            break
        
        if lost[l]-1 == reserve[r] or lost[l]+1 == reserve[r]:
            r += 1
            students += 1
            
            
    
    return n - len(lost) + students
        