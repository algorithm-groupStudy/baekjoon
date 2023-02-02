# 다음에 풀것~
m,n = map(int,input().split())
map_arr=[list(map(int,input().split())) for _ in range(m)]
dp=[[0 for _ in range(n)] for _ in range(m)]
d=[(0,1),(0,-1),(1,0),(-1,0)]
visited=[[False for _ in range(n)] for _ in range(m)]

def dfs(x,y):
    
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<m and 0<=ny<n:
            visited[nx][ny]=True
            

dfs(0,0)
