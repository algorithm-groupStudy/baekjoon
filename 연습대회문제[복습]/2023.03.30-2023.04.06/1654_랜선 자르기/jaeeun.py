# BOJ 1654 랜선 자르기

K, N = map(int, input().split())
nums = [int(input()) for _ in range(K)]
# 이분탐색 오른쪽 범위를 랜선 길이 중 max로 잡아야한다.
target_len = max(nums)

res = 0
l = 1
r = target_len

while l <= r:
    mid = (l + r) // 2
    total = 0
    for num in nums:
        total += num // mid
    if total >= N:
        res = max(res, mid)
        l = mid + 1
    else:
        r = mid - 1

print(res)