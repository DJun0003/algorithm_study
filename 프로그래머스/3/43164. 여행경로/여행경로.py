def dfs(cur, graph, city, num):
    if len(city)-1 == num:
        return True
    
    for i, [des, visit] in enumerate(graph[cur]):
        if not visit:
            graph[cur][i][1] = True
            city.append(des)
            if dfs(graph[cur][i][0], graph, city, num):
                return True
            graph[cur][i][1] = False
            city.pop()
    return False
            
    

def solution(tickets):
    graph = {}
    num_tickets = len(tickets)
    
    for [st, de] in tickets:
        if st in graph:
            graph[st].append([de, False])
        else:
            graph[st] = [[de, False]]
        if not de in graph:
            graph[de] = []
    
    for key in graph.keys():
        graph[key].sort(key=lambda x: x[0])
    
    answer = ['ICN']
    dfs('ICN', graph, answer, num_tickets)
    # print(graph)
    
    return answer