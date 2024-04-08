from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while people:
        p = people.pop()
        answer += 1
        if people and limit - p >= people[0]:
            people.popleft()
        
    return answer