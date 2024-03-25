from collections import deque
def solution(n, lost, reserve):
    answer, len_lost = 0, len(lost)
    lost.sort()
    reserve.sort()
    
    while lost:
        stu = lost.pop(0)
        
        while reserve:
            if reserve[0] >= stu-1:
                break
            reserve.pop(0)
    
        if not reserve:
            break
            
        if stu == reserve[0]:
            len_lost -= 1
            reserve.pop(0)
        elif reserve[0] == stu-1:
            len_lost -= 1
            reserve.pop(0)
            if reserve and reserve[0] == stu:
                reserve.pop(0)
            
        elif reserve[0] == stu+1:
            len_lost -= 1
            reserve.pop(0)
            if lost and lost[0] == stu+1:
                lost.pop(0)
    
    return n-len_lost