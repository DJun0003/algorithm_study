def solution(people, limit):
    people.sort()
    st, fi = 0, len(people)-1
    answer = 0
    
    while st < fi:
        if people[st]+people[fi] <= limit:
            st += 1
        fi -= 1
        answer += 1
    
    if st == fi:
        answer += 1
    
    return answer
        
        