N, M = map(int, input().split())
nums = [] 
for i in range(N):
    nums.append(int(input()))

nums.sort()

start, end = 0, 0
diff = 2000000001

while True:
    if end == N or start == N: 
        break
    elif nums[end] - nums[start] == M:
        diff = M
        break
    elif nums[end] - nums[start] > M:
        diff = min(diff, nums[end] - nums[start])
        start += 1 
    else:
        end += 1

print(diff)