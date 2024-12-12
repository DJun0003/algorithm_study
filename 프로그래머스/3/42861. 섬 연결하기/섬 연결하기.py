def find(a, parents):
    if parents[a] != a:
        parents[a] = find(parents[a], parents)
    return parents[a]

def union(a, b, parents):
    a = find(a, parents)
    b = find(b, parents)
    parents[b] = a

def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x: x[-1])
    
    parents = [i for i in range(n)]
    for s, d, c in costs:
        if find(s, parents) != find(d, parents):
            answer += c
            union(s, d, parents)
    
    return answer