import heapq

def solution(N, road, K):
    answer = 0
    
    graph = [{} for _ in range(N+1)]
    
    for x, y, c in road:
        if y in graph[x]:
            graph[x][y] = min(c, graph[x][y])
            graph[y][x] = min(c, graph[y][x])
        else:
            graph[x][y] = c
            graph[y][x] = c
    
    l = [1e9] * (N+1)
    l[1] = 0
    q = [[0, 1]]
    heapq.heapify(q)
    
    while q:
        cost, cur = heapq.heappop(q)
        
        if l[cur] < cost:
            continue
        
        for des, c in graph[cur].items():
            new_cost = cost+c
            
            if new_cost < l[des]:
                l[des] = new_cost
                heapq.heappush(q, [new_cost, des])
    
    return sum(map(lambda x: x<=K, l))