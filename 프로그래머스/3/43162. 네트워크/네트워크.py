def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i, computers, visited)
            answer += 1

    return answer

def dfs(cur, computers, visited):
    for i in range(len(computers)):
        if i != cur and computers[cur][i] == 1 and visited[i] == False:
            visited[i] = True
            dfs(i, computers, visited)
    
    
    










# def solution(n, computers):
#     answer = 0
#     visited = [False]*n
    
#     for i in range(n):
#         if not visited[i]:
#             DFS(computers, visited, i)
#             # print(i, visited)
#             answer += 1
#     return answer


# def DFS(computers, visited, node):
#     visited[node] = True
    
#     edges = computers[node]
#     for i in range(len(edges)):
#         if edges[i] and not visited[i]:
#             DFS(computers, visited, i)

            
# def DFS(computers, visited, start):
#     stack = [start]
    
#     while stack:
#         node = stack.pop()
#         visited[node] = True
        
#         edges = computers[node]
#         for i in range(len(edges)):
#             if edges[i] and not visited[i]:
#                 stack.append(i)

    