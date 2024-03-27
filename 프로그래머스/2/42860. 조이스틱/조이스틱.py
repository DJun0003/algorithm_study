def solution(name):    
    updown = 0
    a_num, z_num = ord('A'), ord('Z')
    leftright = len(name) - 1
    
    for i, spell in enumerate(name):
        updown += min(ord(spell) - a_num, z_num - ord(spell) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        leftright = min([leftright, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
    
    return updown + leftright