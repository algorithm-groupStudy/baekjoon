# BOJ 17612 쇼핑몰
# Pypy3

import heapq
import sys
input = sys.stdin.readline

# 고객 N명, # 계산대 K개
N, K = map(int, input().split())
cashier = []
# 힙에 [대기시간, 계산대id, 손님리스트]를 넣어준다.
# 대기시간이 같을 경우 계산대 id가 작은 것을 먼저 뽑기 위해 대기시간 대소관계가 바뀌지 않는 정도로 작은 수를 곱해서 넣어준다..
# 초기화: 모든 계산대에 대해 대기시간이 0
for c_id in range(1, K+1):
    heapq.heappush(cashier, [c_id*0.0000001, c_id, []])

# 각 손님에 대하여 가장 대기시간이 작은 계산대를 pop해 대기시간, 손님리스트를 업데이트해 넣어준다.
for idx in range(N):
    i, w = map(int, input().split())
    now = heapq.heappop(cashier)
    now[0] += w
    now[2].append((i, w))
    heapq.heappush(cashier, now)

# out: 우선순위큐에 (각 손님이 나가는 시간, 손님id)를 넣어준다.
out = []
for cash in cashier:
    # 나가는 시간이 동일한 경우 고려 위해 계산대 id가 클 수록 더 작은 수를 더함
    c_id = ((K+1) - cash[1]) * 0.0000001
    prev = 0  # 계산대별로 손님의 나가는 시간 계산 위해 손님들의 계산 시간을 누적해준다.
    for customer in cash[2]:
        heapq.heappush(out, ((customer[1]+prev)+c_id, customer[0]))
        prev += customer[1]

# 손님들이 나가는 id를 순서대로 뽑아 정답 계산
total = 0
for idx in range(1, N+1):
    c_out = heapq.heappop(out)
    total += idx * c_out[1]


print(total)