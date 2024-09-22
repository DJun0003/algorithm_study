def solution(numbers):
    numbers = sorted([str(n) for n in numbers], key=lambda x: x*3,reverse=True)
    answer = ''.join(numbers)
    
    if int(answer) == 0:
        return '0'
    else:
        return answer