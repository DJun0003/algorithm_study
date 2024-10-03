

def solution(triangle):
    
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j:j+2])
    
    return triangle[0][0]