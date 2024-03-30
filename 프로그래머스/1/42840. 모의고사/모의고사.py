def solution(answers):
    s1list = [5,1,2,3,4]
    s2list = [5,2,1,2,3,2,4,2]
    s3list = [5,3,3,1,1,2,2,4,4,5]
    score = [0,0,0]
    
    for i, ans in enumerate(answers):
        score[0] += int(s1list[(i+1)%5] == ans)
        score[1] += int(s2list[(i+1)%8] == ans)
        score[2] += int(s3list[(i+1)%10] == ans)
        
    maxs, answer = max(score), []
    for i in range(3):
        if score[i] == maxs:
            answer.append(i+1)
    return answer