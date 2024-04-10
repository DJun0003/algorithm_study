def solution(n):
    q_list = []
    
    def backtracking(answer):
        if len(q_list) == n:
            return answer+1
        
        for i in range(n):
            cur = True
            for ii, q in enumerate(q_list):
                if i==q or i==q-len(q_list)+ii or i==q+len(q_list)-ii:
                    cur=False
                    break
            
            if cur:
                q_list.append(i)
                answer = backtracking(answer)
                q_list.pop()
        return answer
        
    return backtracking(0)
    