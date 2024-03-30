# from collections import deque
# def solution(begin, target, words):
#     if target not in words:
#         return 0
    
#     nodes = deque([[begin, 0]])
#     while nodes:
#         n, depth = nodes.popleft()
#         if n == target:
#             return depth
        
        
#         for w in words:
#             for i in range(len(n)-1):
#                 if n[:i]+n[i+1:] == w[:i] + w[i+1:]:
#                     nodes.append([w, depth+1])
#             if n[:-1] == w[:-1]:
#                 nodes.append([w, depth+1])
#         print(nodes)
# # solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])


from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [ 0 for i in range(len(words))]
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt+1])
                    V[i] = 1
                    
    return answer