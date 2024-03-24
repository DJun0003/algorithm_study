def solution(citations):
    
    citations.sort(reverse=True)
    for i in range(len(citations)):
        print(citations[i], i+1)
        if citations[i] < i+1:
            return i
    
    return len(citations)

# solution([9,6,7,4,7,1])