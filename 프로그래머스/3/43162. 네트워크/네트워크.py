
def dfs(computers, com, visited):
    
    visited[com] = True
    for i in range(len(computers[com])):
        if computers[com][i] == 1 and not visited[i]:
            dfs(computers, i, visited)

def solution(n, computers):
    ans = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            ans += 1
    
    return ans
        
    