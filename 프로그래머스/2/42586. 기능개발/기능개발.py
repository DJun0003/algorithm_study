import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    pro = deque(progresses)
    sp = deque(speeds)
    
    t_bf, num = math.ceil((100 - pro.popleft())/sp.popleft()), 1
    while len(pro) > 0:
        t = math.ceil((100 - pro.popleft())/sp.popleft())
        if t > t_bf:
            t_bf = t
            answer.append(num)
            num = 1
        else:
            num += 1
        
    
    answer.append(num)
    
    return answer

# def solution(progresses, speeds):
#     Q = []
    
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<math.ceil((100-p)/s):
#             Q.append([math.ceil((100-p)/s), 1])
#         else:
#             Q[-1][1] += 1
        
        
#     return [q[1] for q in Q]