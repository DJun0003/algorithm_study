
N, M = map(int, input().split())
num_list = []

def solution():
    if len(num_list) == M:
        print(' '.join(num_list))
        return
    
    for i in range(1, N+1):
        num_list.append(str(i))
        solution()
        num_list.pop()

solution()