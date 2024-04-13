def solution(n):
    q_list = []

    def backtracking(answer):
        y = len(q_list)
        if y == n:
            return answer + 1
        
        for x in range(n):
            do_append = True
            for qy, qx in enumerate(q_list):
                if x == qx or x == qx+y-qy or x == qx-y+qy:
                    do_append = False
                    break
            if do_append:
                q_list.append(x)
                answer = backtracking(answer)
                q_list.pop()
        return answer
    
    return backtracking(0)























# def solution(n):
#     q_list = []
    
#     def backtracking(answer):
#         if len(q_list) == n:
#             return answer+1
        
#         for i in range(n):
#             cur = True
#             for ii, q in enumerate(q_list):
#                 if i==q or i==q-len(q_list)+ii or i==q+len(q_list)-ii:
#                     cur=False
#                     break
            
#             if cur:
#                 q_list.append(i)
#                 answer = backtracking(answer)
#                 q_list.pop()
#         return answer
        
#     return backtracking(0)
    