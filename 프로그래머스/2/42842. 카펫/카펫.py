def solution(brown, yellow):
    w, h = yellow, 1
    while w >= h:
        if brown == (2*w + 2*h + 4):
            break
        h += 1
        while yellow % h != 0: 
            h += 1
        w  = yellow // h
    
    return [w+2, h+2]