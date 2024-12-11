from itertools import permutations

def solution(numbers):
    ans = set()
    for n in range(1, len(numbers)+1):
        num_list = permutations(numbers, n)
        for str_num in num_list:
            num = int(''.join(str_num))
            if num==0 or num==1:
                continue
                
            sq = int(num ** 0.5)
            
            is_ = False
            for key in range(2, sq+1):
                if (num%key) == 0:
                    is_ = True
                    break
            
            if not is_:
                ans.add(num)
    return len(ans)