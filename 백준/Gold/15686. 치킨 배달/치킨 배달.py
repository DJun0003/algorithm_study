import math

n,m = map(int, input().split())

house = []
chikens = []
j = 0
for _ in range(n):
    l = list(map(int, input().split()))
    for i in range(len(l)):
        if l[i] == 1:
            house.append([j, i])
        elif l[i] == 2:
            chikens.append([j, i])
    j += 1


chiken_list = []
    
def combinations(cur, answer):
    if len(chiken_list) == m:
        total_length = 0
        for home in house:
            min_length = 1e9
            for chiken in chiken_list:
                length = abs(home[0]-chiken[0]) + abs(home[1]-chiken[1])
                if length < min_length:
                    min_length = length
            total_length += min_length
        
        return total_length
    
    for i in range(cur, len(chikens)):
        chiken_list.append(chikens[i])
        cur_length = combinations(i+1, answer)
        if cur_length < answer:
            answer = cur_length
        chiken_list.pop()
    
    return answer

print(combinations(0, 1e9))
    