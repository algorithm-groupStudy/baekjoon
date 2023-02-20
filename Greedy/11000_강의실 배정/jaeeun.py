# BOJ 11000
# 강의실 배정 (코드 참고)

import heapq
import sys

N = int(input())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

classes.sort(key=lambda x: x[0])
clroom = []
heapq.heappush(clroom, classes[0][1])

for idx in range(1, N):
    if classes[idx][0] >= clroom[0]:
        heapq.heappop(clroom)
    heapq.heappush(clroom, classes[idx][1])

print(len(clroom))

# 시작시간 기준 정렬 후 종료 시간을 우선순위 큐에 삽입 (heapq 이용)
# 종료시간 가장 빠른 수업과 시작시간 비교
# input은 sys.stdin.readline으로..

