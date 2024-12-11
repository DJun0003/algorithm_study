def solution(numbers):
    answer = ''.join(sorted([str(n) for n in numbers], key=lambda x: x*3 ,reverse=True))
    if int(answer)==0:
        answer = '0'
    return answer