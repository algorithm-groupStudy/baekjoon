# 돌의 개수 N 
N = int(input())
# N개의 돌에 적힌 수를 담은 배열 nums
nums = list(map(int, input().split()))

# 배열 dp[i]에 i번째 돌까지 이동할 때의 K의 최솟값을 저장 
dp = [0] * N

# idx에 대하여 (예: idx = 3)
for idx in range(1, N):
    tmp = []
    # k = 1, 2, 3
    # idx 0 -> 2 -> 3 로 건너가는 경우 필요한 최대 힘은 dp[2]와 2 -> 3에 필요한 힘 중 최댓값  
    # idx 0 -> 1 -> 3 로 건너가는 경우 필요한 최대 힘은 dp[1]과 1 -> 3에 필요한 힘 중 최댓값 
    # idx 0 -> 3 로 건너가는 경우 필요한 최대 힘은 dp[0] (0)과  0 -> 3에 필요한 힘 중 최댓값  
    # 위 세 가지 경우 중 최솟값을 dp[3]에 저장한다. 
  
    for k in range(1, idx + 1):
        tmp.append(max(dp[idx-k], k * (abs(nums[idx] - nums[idx-k]) + 1)))
    dp[idx] = min(tmp)

# 마지막 돌에 도달했을 때 필요한 K의 최솟값을 출력 
print(dp[-1])