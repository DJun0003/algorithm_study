from collections import deque

def solution(prices):
    num_prices = len(prices)
    answer = [num_prices-i-1 for i in range(num_prices)]
    prices = deque(prices)
    q = deque()
    step = 0
    
    
    for i in range(num_prices):
        p = prices.popleft()
        
        while len(q) > 0:
            if q[-1][0] > p:
                _, idx = q.pop()
                answer[idx] -= num_prices-i-1
            else:
                break
        q.append((p, i))
                    
    return answer