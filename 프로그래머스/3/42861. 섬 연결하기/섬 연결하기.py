def find(x, parents):
    if x!= parents[x]:
        parents[x] = find(parents[x], parents)
    
    return parents[x]

def union(st, de, parents):
    st = find(st, parents)
    de = find(de, parents)
    
    parents[de] = st
    


def solution(n, costs):
    costs.sort(key=lambda x: x[-1])
    parents = [i for i in range(n)]
    answer = 0
    
    for [st, de, c] in costs:
        if find(st, parents) != find(de, parents):
            answer += c
            union(st, de, parents)
    
    return answer
    