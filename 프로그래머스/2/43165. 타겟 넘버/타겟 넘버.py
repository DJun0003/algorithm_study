from collections import deque


def solution(numbers, target):
    
    adds = deque([0])
    
    for num in numbers:
        l = len(adds)
        for i in range(l):
            a = adds.popleft()
            adds.append(a+num)
            adds.append(a-num)
    
    
    return adds.count(target)
    









# # BFS -> 303ms, 50.1MB
# def solution(numbers, target):
#     answer = 0
#     leaves = [0]
    
#     for num in numbers:
#         tmp = []
#         for parent in leaves:
#             tmp.append(parent + num)
#             tmp.append(parent - num)
#         leaves = tmp
    
#     answer = sum(map(lambda x: x == target, leaves))
    
#     return answer


# # DFS -> 834ms
# def solution(numbers, target):
#     answer = DFS(numbers, target, 0)
#     return answer

# def DFS(numbers, target, depth):
#     answer = 0
#     if depth == len(numbers):
#         if sum(numbers) == target:
#             return 1
#         else:
#             return 0
    
#     else:
#         answer += DFS(numbers, target, depth+1)
#         numbers[depth] *= -1
#         answer += DFS(numbers, target, depth+1)
#         return answer

# # 짧은코드 -> 355ms, 34.1MB
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     a = list(map(sum, product(*l)))
#     return a.count(target)

            