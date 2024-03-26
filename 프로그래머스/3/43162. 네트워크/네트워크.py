def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if not visited[i]:
            DFS(computers, visited, i)
            # print(i, visited)
            answer += 1
    return answer


def DFS(computers, visited, node):
    visited[node] = True
    
    edges = computers[node]
    for i in range(len(edges)):
        if edges[i] and not visited[i]:
            DFS(computers, visited, i)
    