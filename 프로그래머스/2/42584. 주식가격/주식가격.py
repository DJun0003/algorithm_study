from collections import deque

# def solution(prices):
#     num_prices = len(prices)
#     answer = [num_prices-i-1 for i in range(num_prices)]
#     prices = deque(prices)
#     q = deque()
#     step = 0
    
    
#     for i in range(num_prices):
#         p = prices.popleft()
        
#         while len(q) > 0:
#             if q[-1][0] > p:
#                 _, idx = q.pop()
#                 answer[idx] -= num_prices-i-1
#             else:
#                 break
#         q.append((p, i))
                    
#     return answer


def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer