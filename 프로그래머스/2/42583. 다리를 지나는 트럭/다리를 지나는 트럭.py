from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    waits = deque([[truck_weights.popleft(), 1]])
    time = 1
    
    while truck_weights:
        time += 1
        
        for w in waits:
            w[1] += 1
        
        if waits[0][1] == bridge_length+1:
            waits.popleft()
            
        if len(waits) < bridge_length and sum(w[0] for w in waits)+truck_weights[0] <= weight:
            waits.append([truck_weights.popleft(),1])
        # print(time, waits, truck_weights)
    
    if waits:
        time += bridge_length - waits[-1][1] +1
    
    return time
        