def solution(participant, completion):
    com_dict = {}
    for c in completion:
        if c in com_dict.keys():
            com_dict[c] += 1
        else:
            com_dict[c] = 1
    
    for p in participant:
        v = com_dict.get(p, 0)
        if v == 0:
            return p
        else:
            com_dict[p] -= 1
        
        
        