def solution(number, k):
    answer = [number[0]]
    for i, num in enumerate(number[1:]):
        while answer and k and answer[-1] < num:
            answer.pop()
            k -= 1
        
        answer.append(num)
    
    if k:
        answer = answer[:-k]
    
    return ''.join(answer)
        
