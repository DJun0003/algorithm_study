from heapq import heappush, heappop, heapify

def solution(operations):
    answer = []
    heap = []
    max_heap = []
    min_heap = []
    
    for op in operations:
        if op == 'D 1' and max_heap:
            heappop(max_heap)
            min_heap = []
            for i in range(len(max_heap)):
                heappush(min_heap, -max_heap[i])
        elif op == 'D -1' and min_heap:
            heappop(min_heap)
            max_heap = []
            for i in range(len(min_heap)):
                heappush(max_heap, -min_heap[i])
        elif op[0] == 'I':
            heappush(min_heap, int(op[2:]))
            heappush(max_heap, -int(op[2:]))
        # print(op, min_heap, max_heap)
    
    if min_heap:
        return [-heappop(max_heap), heappop(min_heap)]
    else:
        return [0, 0]
    