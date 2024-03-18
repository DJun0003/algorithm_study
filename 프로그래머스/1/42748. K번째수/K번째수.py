def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        val = sorted(array[i-1:j])[k-1]
        answer.append(val)
        
    return answer