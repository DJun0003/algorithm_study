def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    cur_nodes = set([costs[0][0]])
    
    while len(cur_nodes) != n:
        for [n1, n2, cost] in costs:
            if (n1 in cur_nodes) and (n2 in cur_nodes):
                continue
            if (n1 in cur_nodes) or (n2 in cur_nodes):
                cur_nodes |= set([n1, n2])
                answer += cost
                break
            
    return answer