from heapq import heappush, heappop

def solution(N, road, K):
    answer = 0

    graph = [{} for _ in range(N+1)]
    for a, b, c in road:
        if b in graph[a]:
            graph[a][b] = min(c, graph[a][b])
            graph[b][a] = min(c, graph[b][a])
        else:
            graph[a][b] = c
            graph[b][a] = c
    
    q = []
    heappush(q, [0, 1])
    length = [1e9] * (N+1)
    length[1] = 0
    
    while q:
        cost, cur = heappop(q)
        
        if length[cur] < cost:
            continue
        
        for des, c in graph[cur].items():
            new_c = cost+c
            if new_c < length[des]:
                length[des] = new_c
                heappush(q, [new_c, des])
    

    return sum(map(lambda x: x<=K, length))