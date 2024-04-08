import sys
from collections import deque

def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for n in range(len(graph)):
        if graph[node][n] == 1 and not visited[n]:
            dfs(graph, n, visited)

def bfs(graph, start):
    visited = [False] * (len(graph)+1)
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')

    while queue:
        node = queue.popleft()
        for n in range(len(graph)):
            if graph[node][n] == 1 and not visited[n]:
                visited[n] = True
                print(n, end=' ')
                queue.append(n)





n, m, v = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

dfs_visited = [False] * (n+1)
dfs(graph, v, dfs_visited)
print()
bfs(graph, v)