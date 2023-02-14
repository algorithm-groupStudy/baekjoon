import heapq
t = int(input())
for tc in range(t):
    n = int(input())
    cd_lst = list(map(int, input().split()))
    heap = []
    total = 0
    for cd in cd_lst:
        heapq.heappush(heap, cd)

    while len(heap) > 1:
        cd1 = heapq.heappop(heap)
        cd2 = heapq.heappop(heap)
        total = total+cd1+cd2
        heapq.heappush(heap, cd1+cd2)

    print(total)
