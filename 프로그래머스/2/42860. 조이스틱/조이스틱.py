def solution(name):
    n = len(name)
    ord_a, ord_z = ord('A'), ord('Z')
    
    leftright = n-1
    answer = 0
    for i, ch in enumerate(name):
        updown = min(ord(ch)-ord_a, ord_z-ord(ch)+1)
        answer += updown
        
        next = i+1
        while next<n and name[next] == 'A':
            next += 1
        
        leftright = min(leftright, (2*i) + (n-next), 2*(n-next) + i)
    
    answer += leftright
    return answer