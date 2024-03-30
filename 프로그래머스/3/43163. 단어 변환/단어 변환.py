from collections import deque

# def solution(begin, target, words):
#     if target not in words:
#         return 0
    
#     nodes = deque([[begin, 0]])
#     v = [False] * len(words)
#     while nodes:
#         n, depth = nodes.popleft()
#         if n == target:
#             return depth
        
#         for i, w in enumerate(words):
#             if not v[i]:
#                 cnt = 0
#                 for ii in range(len(n)):
#                     if n[ii] != w[ii]:
#                         cnt += 1
#                 if cnt == 1:
#                     nodes.append([w, depth+1])
#                     v[i] = True
#     return 0

def solution(begin, target, words):
    
    if target not in words : 
        return  0
    
    return bfs(begin, target, words)


#최소 단계를 찾아야 하므로 bfs
def bfs(begin, target, words):

    queue = deque()
    queue.append([begin, 0]) #시작 단어와 단계 0으로 초기화
    
    while queue:
        now, step = queue.popleft()
        
        if now == target:
            return step
        
        #단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            count = 0
            for i in range(len(now)): #단어의 길이만큼 반복하여
                if now[i] != word[i]: #단어에 알파벳 한개씩 체크하기
                    count += 1
                    
            if count == 1: 
                queue.append([word, step+1])
# solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])