def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
        
    return parents[x]

def union(x, y, parents):
    x = find(x, parents)
    y = find(y, parents)
    
    parents[y] = x

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[-1])
    
    parents = [i for i in range(n)]
    
    for [x,y,c] in costs:
        if find(x, parents) != find(y, parents):
            union(x, y, parents)
            answer += c
    
    
    return answer