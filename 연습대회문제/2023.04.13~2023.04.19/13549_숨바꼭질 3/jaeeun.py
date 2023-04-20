# BOJ 13549 숨바꼭질 3 
# BFS + 우선순위 큐 사용 
# 0-1 너비 우선 탐색을 사용할 수 있다고 한다. 

import heapq 

def bfs(start):
    q = []
    # 우선순위 큐에서 방문시간을 기준으로 정렬되도록 한다 (시작점은 0초)
    heapq.heappush(q, (0,start))
    visited[start] = 0 

    while q: 
        now_t, now = heapq.heappop(q)
        if now == K:  # 여기서 도착 여부 확인 
            return now_t 

        for k in range(3):
            if k == 0: 
                new = 2 * now 
                new_t = now_t 
            elif k == 1: 
                new = now + 1 
                new_t = now_t + 1 
            else: 
                new = now - 1 
                new_t = now_t + 1 

            if 0 <= new < 100001 and visited[new] == -1: # 여기서 new == K로 도착 여부를 확인할 경우, 도착시간이 더 느린 경우가 먼저 확인될 수 있으므로 우선순위 큐에서 꺼낼 때 확인해야 한다 
                visited[new] = new_t 
                heapq.heappush(q, (new_t, new))
    return -1 
        

N, K = map(int, input().split())
# 방문시간 -1로 초기화 
visited = [-1 for _ in range(100001)]
res = bfs(N)
print(res)