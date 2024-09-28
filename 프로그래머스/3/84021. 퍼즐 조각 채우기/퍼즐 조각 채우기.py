
def near_box(board, cur, ch_num, box_list, min_idx, max_idx):
    box_list.append(cur)
    board[cur[0]][cur[1]] = 0 if ch_num==1 else 1
    min_idx[0] = cur[0] if cur[0] < min_idx[0] else min_idx[0]
    min_idx[1] = cur[1] if cur[1] < min_idx[1] else min_idx[1]
    max_idx[0] = cur[0] if cur[0] > max_idx[0] else max_idx[0]
    max_idx[1] = cur[1] if cur[1] > max_idx[1] else max_idx[1]
    
    for (y, x) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ny, nx = cur[0] + y, cur[1] + x
        if ny<len(board) and ny>-1 and nx<len(board) and nx>-1 and board[ny][nx] == ch_num:
            box_list, min_idx, max_idx = near_box(board, [ny, nx], ch_num, box_list, min_idx, max_idx)
            
    
    return box_list, min_idx, max_idx


def search(board, ch_num):
    l = len(board)
    all_boxes = []
    
    for i in range(l):
        for j in range(l):
            if board[i][j] == ch_num:
                box_idx, min_idx, max_idx = near_box(board, [i,j], ch_num, [], [i,j], [i,j])
                cur_box = [[0]*(max_idx[1]-min_idx[1]+1) for _ in range(max_idx[0]-min_idx[0]+1)]
                for [y,x] in box_idx:
                    cur_box[y-min_idx[0]][x-min_idx[1]] = 1
                all_boxes.append(cur_box)
    return all_boxes
    

def rotation(box):
    rot_box = []
    for x in range(len(box[0])):
        rot_y = []
        for y in range(len(box)-1, -1, -1):
            rot_y.append(box[y][x])
        rot_box.append(rot_y)
    return rot_box
    
def solution(game_board, table):
    
    board_box = search(game_board, 0)
    table_box = search(table, 1)
    visited = [0] * len(table_box)
    answer = 0
    
    for ii, b in enumerate(board_box):
        is_visit = False
        
        for i, t in enumerate(table_box):
            if is_visit or sum(visited) == len(table_box):
                break
            
            if visited[i] == 0:
                for _ in range(4):
                    if b == t:
                        visited[i] = 1
                        answer += sum(list(sum(s) for s in b))
                        is_visit = True
                        break
                    t = rotation(t)
    
    return answer
            