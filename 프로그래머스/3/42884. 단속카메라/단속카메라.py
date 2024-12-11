def solution(routes):
    routes.sort()
    cameras = [routes[0]]
    for r in routes[1:]:
        max_len, max_idx = -1, -1
        
        for i, cam in enumerate(cameras):
            if cam[0]>r[1] or cam[1]<r[0]:
                continue
            else:
                cur_len = min(cam[1], r[1]) - max(cam[0], r[0])
                if max_len < cur_len:
                    max_idx = i
                    max_len = cur_len
        
        if max_idx != -1:
            cameras[max_idx][0] = max(cameras[i][0], r[0])
            cameras[max_idx][1] = min(cameras[i][1], r[1])
        
        else:
            cameras.append(r)
    
    return len(cameras)