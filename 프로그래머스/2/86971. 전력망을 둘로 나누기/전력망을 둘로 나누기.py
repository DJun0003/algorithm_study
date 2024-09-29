from collections import deque
def search(n, wires):
    visited = [0] * n
    ans = []
    
    for i in range(n):
        if visited[i] == 0:
            q = deque([i])
            visited[i] = 1
            num = 0
            while q:
                cur = q.popleft()
                num += 1
                for new in wires[cur]:
                    if visited[new] == 0:
                        visited[new] = 1
                        q.append(new)
            ans.append(num)
            
    return max(ans)-min(ans)
        


def solution(n, wires):
    wires = deque(wires)
    l = len(wires)
    answer = 100
    for _ in range(l):
        del_wire = wires.popleft()
        cur_wires = [[] for _ in range(n)]
        for j in range(l-1):
            v1, v2 = wires[j]
            cur_wires[v1-1].append(v2-1)
            cur_wires[v2-1].append(v1-1)
        diff = search(n, cur_wires)
        if diff < answer:
            answer = diff
        wires.append(del_wire)
        
    return answer