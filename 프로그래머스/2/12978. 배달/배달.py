import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    
    for [n1, n2, c] in road:
        graph[n1].append([n2, c])
        graph[n2].append([n1, c])
    
    q = [[0, 1]]
    heapq.heapify(q)
    length = [1e9] * (N+1)
    length[1] = 0
    
    while q:
        cost, cur = heapq.heappop(q)
        
        if length[cur] < cost:
            continue
        
        for [des, c] in graph[cur]:
            if cost+c < length[des]:
                length[des] = cost+c
                heapq.heappush(q, [cost+c, des])
        
    return sum(map(lambda x: x<=K, length))