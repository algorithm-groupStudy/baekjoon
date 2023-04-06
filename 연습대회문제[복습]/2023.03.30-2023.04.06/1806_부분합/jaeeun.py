# BOJ 1806 부분합

N, S = map(int, input().split())
nums = list(map(int, input().split()))

# l, r 포인터를 정해서 부분합이 S 이상이면 l을 1 증가, 미만이면 r을 1 증가하여 합이 S 이상이 되는 것을 찾음
# 그 중 길이 (r-l)가 가장 짧은 것을 정답으로 한다. 
l = r = -1
total = 0
min_length = float('inf')

while True:
    if total < S:
        r += 1
        if r >= N:
            break
        total += nums[r]
    elif total >= S:
        min_length = min(min_length, r-l)
        l += 1
        total -= nums[l]

if min_length == float('inf'):
    print(0)
else:
    print(min_length)