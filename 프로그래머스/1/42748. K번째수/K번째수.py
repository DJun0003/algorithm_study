def solution(array, commands):
    ans = []
    
    for com in commands:
        arr = sorted(array[com[0]-1:com[1]])
        ans.append(arr[com[2]-1])
    
    return ans