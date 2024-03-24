def solution(numbers):
    ans = ''
    
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    
    for n in numbers:
        ans += n
    
    
    return str(int(ans))