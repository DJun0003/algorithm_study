from collections import deque

def solution(tickets):
    dic = {}
    for [f,t] in tickets:
        if f in dic:
            dic[f].append([False, t])
        else:
            dic[f] = [[False, t]]
        if t not in dic:
            dic[t] = []
        
    for v in dic.values():
        v.sort(key=lambda x: x[1])
    
    des_list = ['ICN']
    
    def dfs(cur, use):
        if use == len(tickets):
            return True
        
        for tic in dic[cur]:
            if not tic[0]:
                tic[0] = True
                des_list.append(tic[1])
                
                finish = dfs(tic[1], use+1)
                if finish:
                    return True
                
                tic[0] = False
                des_list.pop()
        return False
    
    dfs('ICN', 0)
    return des_list
    
    
    
            