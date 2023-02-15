import sys
sys.stdin = open('input.txt')
import heapq

t = int(input())

for test_case in range(1,t+1):
    nums_chapter = int(input())
    cost_list = list(map(int, input().split()))
    min_cost = 0
    q = []
    for cost in cost_list:
        heapq.heappush(q, cost)
    # [1, 3, 3, 4, 5, 14, 5, 21, 4, 5, 98, 35, 21, 17, 32]
    while len(q) > 1:
        # 최소 cost 두개 pop 후 더함 
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        min_cost += a + b
        # 더한 값을 q에 다시 push
        heapq.heappush(q, a+b)
    print(min_cost)
    