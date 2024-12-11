def solution(word):
    answer = 0
    w_list = ['A', 'E', 'I', 'O', 'U']
    for i, cur in enumerate(word):
        for w in w_list:
            if w < cur:
                answer += 1
                for n in range(1, 5-i):
                    answer += 5**n
            
            elif w == cur:
                answer += 1
                break
    
    return answer