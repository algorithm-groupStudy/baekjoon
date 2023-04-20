# BOJ 10971 외판원순회 

# cnt: 선택한 도시 개수-1, total: 비용, prev: 이전에 선택한 도시, start: 출발 도시 
def sol(cnt, total, prev, start):
    global min_total
    if total >= min_total: 
        return  
    if cnt == N-1:  # N개 도시 다 선택한 경우 
        if arr[prev][start]: # 마지막 도시에서 출발 도시로 돌아와야함 (연결되어있는지 확인 후 비용 더해줌)
            total += arr[prev][start]
            min_total = min(min_total, total)
        return 
    else:
        for k in range(N):
            if arr[prev][k] > 0 and visited[k] == 0:  # k도시가 연결되어있고 방문한 적 없을 경우 
                visited[k] = 1  
                sol(cnt+1, total+arr[prev][k], k, start)
                visited[k] = 0  


N = int(input())  # 도시의 수 N개
arr = [list(map(int, input().split())) for _ in range(N)]  # 비용행렬 
min_total = 100000000
visited = [0 for _ in range(N)]  # 방문한 도시 체크 
for k in range(N):  # 시작하는 도시가 1번~N번일 경우를 각각 따져준다. 
    visited[k] = 1
    sol(0, 0, k, k)
    visited[k] = 0 
print(min_total)