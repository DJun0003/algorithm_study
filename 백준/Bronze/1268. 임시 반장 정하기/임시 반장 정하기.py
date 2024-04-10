import sys

n = int(input())
classes = []
for i in range(n):
    classes.append(list(map(int, sys.stdin.readline().split())))

nums = [[0] * n for _ in range(n)]
for i in range(5):
    for s in range(n):
        for ss in range(s+1, n):
            if nums[s][ss] == 0 and classes[s][i] == classes[ss][i]:
                nums[s][ss] = nums[ss][s] = 1

max_idx, max_num = -1, -1
for i in range(n):
    num = sum(nums[i])
    if num > max_num:
        max_idx = i
        max_num = num

print(max_idx+1)