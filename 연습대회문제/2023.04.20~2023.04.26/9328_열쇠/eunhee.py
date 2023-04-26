from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]


def bfs(c_x, c_y):
    visited= [[False for _ in range(w+2)] for _ in range(h+2)]
    visited[c_x][c_y]=True
    q = deque([(c_x,c_y)])
    door_graph = [deque() for _ in range(26)]
    cnt=0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<h+2 and 0<=ny<w+2 and not visited[nx][ny]:
                visited[nx][ny]=True
                if map_lst[nx][ny]=="*":
                    continue
                if ord("A")<=ord(map_lst[nx][ny])<=ord("Z"):
                    k = ord(map_lst[nx][ny])-ord("A")
                    if not key[k]==1:
                        door_graph[k].append((nx,ny))
                        continue
                elif ord("a")<=ord(map_lst[nx][ny])<=ord("z"):
                    k=ord(map_lst[nx][ny])-ord("a")
                    key[k]=1
                    while door_graph[k]:
                        door_x,door_y = door_graph[k].popleft()
                        q.append((door_x,door_y))
                elif map_lst[nx][ny]=="$":
                    cnt+=1
                q.append((nx,ny))
    print(cnt)    


tc = int(input())
for _ in range(tc):
    h,w = map(int,input().split())
    map_lst = [list("."+input()+".") for _ in range(h)]
    map_lst.insert(0,["." for _ in range(w+2)])
    map_lst.append(["." for _ in range(w+2)])
    key = [0 for _ in range(26)]
    for k in input():
        if k=="0":
            break
        key[ord(k)-ord("a")]=1
    
    bfs(0,0)

