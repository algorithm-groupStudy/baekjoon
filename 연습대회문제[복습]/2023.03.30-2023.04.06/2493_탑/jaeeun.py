# BOJ 2493 탑

N = int(input())
nums = list(map(int, input().split()))
# tmp: 원소 오른쪽의 (탑 높이, 탑 id) 저장 (제일 왼쪽이 제일 마지막 원소)
tmp = []
# res: 신호를 수신한 탑들의 번호를 저장
res = [0 for _ in range(N)]

for idx in range(N-1, -1, -1):
    while tmp:
        if tmp[-1][0] < nums[idx]:
            res[tmp[-1][1]] = idx+1  # 부딪히면 idx 저장 (idx는 1부터 시작)
            tmp.pop()
        else:
            break

    tmp.append((nums[idx], idx))

print(*res)