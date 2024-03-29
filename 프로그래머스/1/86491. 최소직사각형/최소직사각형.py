def solution(sizes):
    curs = [0,0]
    answer = 0
    
    for s in sizes:
        if s[0] < s[1]:
            s.reverse()
        
        if curs[0] < s[0]:
            curs[0] = s[0]
        if curs[1] < s[1]:
            curs[1] = s[1]
        answer = curs[0] * curs[1]
        
        
    return answer