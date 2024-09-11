def solution(answers):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if a1[i%len(a1)] == ans:
            score[0] += 1
        if a2[i%len(a2)] == ans:
            score[1] += 1
        if a3[i%len(a3)] == ans:
            score[2] += 1
    
    max_score = max(score)
    answer = []
    for i in range(len(score)):
        if score[i] == max_score:
            answer.append(i+1)
    return answer