def solution(number, k):
    answer = [number[0]]
    for i, n in enumerate(number[1:]):
        while k and answer and n > answer[-1]:
            answer.pop()
            k -= 1
            
        # if k == 0:
        #     answer = ''.join(answer) + number[i+1:]
        #     break
        
        answer.append(n)
    
    if k > 0:
        answer = answer[:-k]
    
    return ''.join(answer)