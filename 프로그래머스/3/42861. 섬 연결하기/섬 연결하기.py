def find_parents(cur, parents):
    if parents[cur] == cur:
        return cur
    else:
        return find_parents(parents[cur], parents)

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: [x[2], x[0], x[1]])
    parents = list(range(n))
    num_edges = 0
    
    for [n1, n2, cost] in costs:
        p1, p2 = find_parents(n1, parents), find_parents(n2, parents)
        if  p1 != p2:
            answer += cost
            parents[p2] = p1
            num_edges += 1
        if num_edges == n-1:
            break
            
    return answer

