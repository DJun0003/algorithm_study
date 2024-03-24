from collections import deque
def solution(bridge_length, weight, truck_weights):
    cur_time, cur_weight = 0, 0
    on_bridge = deque()
    truck_weights = deque(truck_weights)
    
    while True:
        cur_time += 1
        
        sum_weight = 0
        while True:
            if  len(on_bridge) > 0 and on_bridge[0][1] >= bridge_length:
                on_bridge.popleft()
            else:
                for i in range(len(on_bridge)):
                    sum_weight += on_bridge[i][0]
                    on_bridge[i][1] += 1
                break
        
        try:
            w = truck_weights.popleft()
            if sum_weight + w <= weight:
                on_bridge.append([w,1])
            else:
                truck_weights.appendleft(w)
        except:
            pass
            
        # print(cur_time, on_bridge, sum_weight)
        
        if len(on_bridge) == 0 and len(truck_weights) == 0:
            break
        
    
    return cur_time