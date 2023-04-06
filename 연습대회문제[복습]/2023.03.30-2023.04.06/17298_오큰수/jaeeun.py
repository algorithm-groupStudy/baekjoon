# BOJ 17298 오큰수

N = int(input())
nums = list(map(int, input().split()))
# tmp: 각 원소의 오른쪽 수를 저장 (가장 왼쪽의 수가 마지막 원소가 됨)
tmp = []
# res: 각 원소의 오큰수를 저장
res = [-1 for _ in range(N)]

for idx in range(N-1, -1, -1):
    while tmp:
        if tmp[-1] > nums[idx]:
            res[idx] = tmp[-1]
            break
        else:
            tmp.pop()  # 각 원소의 오른쪽 수가 원소보다 작으면 그 앞 원소에 대해서도 오큰수가 될 수 없으므로 pop
    if not tmp:
        res[idx] = -1
    tmp.append(nums[idx])

print(*res)
