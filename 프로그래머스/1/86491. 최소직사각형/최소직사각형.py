def solution(sizes):
    w, h = 0, 0
    for s in sizes:
        s.sort()
        w = s[0] if s[0] > w else w
        h = s[1] if s[1] > h else h
    
    return w*h