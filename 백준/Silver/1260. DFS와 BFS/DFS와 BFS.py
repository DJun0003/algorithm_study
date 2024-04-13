import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for i in range(1, n+1):
    graph[i].sort()
    
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs(node):
    visited1[node] = True
    print(node, end=' ')
 
    for n2 in graph[node]:
        if visited1[n2] == False:
            dfs(n2)

def bfs():
    queue = deque([v])
    visited2[v] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')        
        
        for n2 in graph[node]:
            if visited2[n2] == False:
                visited2[n2] = True
                queue.append(n2)

dfs(v)
print()
bfs()
    