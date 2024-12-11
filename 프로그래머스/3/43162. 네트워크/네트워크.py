
def dfs(cur, computers, visited):
    visited[cur] = True
    for i in range(len(computers[cur])):
        if computers[cur][i]==1 and not visited[i]:
            dfs(i, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            answer += 1
    return answer