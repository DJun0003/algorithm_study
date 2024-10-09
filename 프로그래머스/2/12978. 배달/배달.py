from heapq import heappush, heappop
def solution(N, road, K):
    graph = [{} for _ in range(N+1)]
    for a,b,c in road:
        if b in graph[a]:
            graph[a][b] = min(c, graph[a][b])
            graph[b][a] = min(c, graph[b][a])
        else:
            graph[a][b] = c
            graph[b][a] = c
    
    q = [[1, 0]]
    costs = [1e9] * (N+1)
    costs[1] = 0
    
    while q:
        cur, c = heappop(q)
        if c>costs[cur]:
            continue
        for des, w in graph[cur].items():
            n_c = c+w
            if n_c<costs[des]:
                costs[des] = n_c
                heappush(q, [des,n_c])
    
    answer = 0
    for c in costs:
        if c <= K:
            answer += 1
    return answer