from itertools import combinations

def solution(N, number):
    num_list = [set() for _ in range(9)]
    for i in range(1, 9):
        cur_nums = set([int(str(N)*i)])
        for j in range(1, i):
            for n1 in num_list[i-j]:
                for n2 in num_list[j]:
                    cal_list = [n1+n2, n1*n2]
                    if n1-n2 > 0:
                        cal_list.append(n1-n2)
                    if n2 != 0 and n1%n2 == 0:
                        cal_list.append(n1/n2)
                    cur_nums.update(cal_list)
        if number in cur_nums:
            return i
        
        num_list[i].update(cur_nums)
    
    return -1
                    