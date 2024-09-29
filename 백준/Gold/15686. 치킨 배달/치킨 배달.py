from itertools import combinations
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

chikens = combinations(chikens, m)
answer = math.inf

for cur_chikens in chikens:
    total_lenght = 0
    for home in house:
        min_length = n*n
        for chiken in cur_chikens:
            length = abs(chiken[0]-home[0]) + abs(chiken[1]-home[1])
            if length < min_length:
                min_length = length
        total_lenght += min_length
    
    if answer > total_lenght:
        answer = total_lenght

print(answer)

