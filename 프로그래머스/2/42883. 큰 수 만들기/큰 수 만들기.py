import time
def solution(number, k):
    answer = [number[0]]
    
    for i, n in enumerate(number[1:]):
        while answer and k and answer[-1] < n:
            answer.pop()
            k -= 1
        
        answer.append(n)
        
        # if k == 0:
        #     if i < len(number)-1:
        #         answer = answer + number[i+1:]
        #     break
    
    if k > 0:
        answer = answer[:-k]
    
    return ''.join(answer)

