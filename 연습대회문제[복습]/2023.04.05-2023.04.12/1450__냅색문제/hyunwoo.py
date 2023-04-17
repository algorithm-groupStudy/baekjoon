import sys
input = sys.stdin.readline

N, C = map(int, input().split())
num_list = list(map(int, input().split()))

left_list = num_list[:N//2]
right_list = num_list[N//2:]

left_sum = []
right_sum = []

# (N/2)*2^(N/2)
for i in range(2**(len(left_list))):
    subset = bin(i)[2:].zfill(len(left_list))
    sum = 0
    for j in range(len(subset)):
        if subset[j] == '1':
            sum += left_list[j]
    left_sum.append(sum)

# (N/2)*2^(N/2)
for i in range(2**(len(right_list))):
    subset = bin(i)[2:].zfill(len(right_list))
    sum = 0
    for j in range(len(subset)):
        if subset[j] == '1':
            sum += right_list[j]
    right_sum.append(sum)

# N*log(N)
right_sum.sort()

cnt = 0

# (N/2)*log(N/2)
for num in left_sum:
    if num > C:
        continue
    target = C-num
    left = 0
    right = len(right_sum)
    while left < right:
        mid = (left+right)//2
        if right_sum[mid] > target:
            right = mid
        else:
            left = mid+1
    cnt += right

print(cnt)