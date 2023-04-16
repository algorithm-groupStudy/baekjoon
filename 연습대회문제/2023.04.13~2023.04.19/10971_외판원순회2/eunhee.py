def dfs(depth, path, total):
    global result
    if total>result:
        return
    if depth==N:
        spend = map_list[path[-1]][path[0]]
        if spend:
            total +=map_list[path[-1]][path[0]]
            result = min(result, total)
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            path.append(i)
            spend = map_list[path[-2]][path[-1]]
            if spend:
                dfs(depth+1,path, total+spend)
            path.pop()
            visited[i]=False


N=int(input())
result = float("INF")
map_list = [list(map(int,input().split())) for _ in range(N)]
visited = [False for _ in range(N)]

for i in range(N):
    visited[i]=True
    dfs(1,[i],0)
    visited[i]=False

print(result)