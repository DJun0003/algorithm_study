import time
def solution(number, k):
    start = time.time()
    max_idx, max_num = 0, number[0]
    for i in range(1, len(number)):
        if max_num < number[i]:
            max_idx, max_num = i, number[i]
    if max_idx <= k:
        number = number[max_idx:]
        k -= max_idx
            
            
    while k>0:
        for i in range(len(number)):
            if i == len(number) - 1:
                number = number[:-1]
                k -= 1
                break
            else:
                if number[i] < number[i+1]:
                    number = number[:i] + number[i+1:]
                    k -= 1
                    break
    end = time.time()
    print('%.2fms'%((end-start)*1e6))
    return number

