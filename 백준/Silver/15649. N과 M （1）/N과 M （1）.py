n, m = map(int, input().split())

answer = []

def solution():
    if len(answer) == m:
        print(*answer)
        return
    
    for i in range(n):
        if not answer or (i+1) not in answer:
            answer.append(i+1)
            solution()
            answer.pop()
    

solution()