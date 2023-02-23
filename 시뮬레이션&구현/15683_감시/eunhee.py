from collections import deque
import copy
def first(cur_x,cur_y, map_lst):
    
    max_cnt =0 
    max_lst=map_lst[:]
    
    for dx, dy in d:
        queue = deque([(cur_x,cur_y)])
        cnt=0
        map_lst_copy = copy.deepcopy(map_lst)
        while queue:
            x, y = queue.popleft()
            nx, ny = dx + x, dy + y
            if 0<=nx<h and 0<=ny<w:
                if map_lst_copy[nx][ny]==6:
                    break
                elif map_lst_copy[nx][ny]!=0:
                    queue.append((nx,ny))
                    continue
                cnt+=1
                map_lst_copy[nx][ny]="#"
                queue.append((nx,ny))
        if max_cnt<cnt : 
            max_cnt=cnt
            max_lst = map_lst_copy[:]
    return max_cnt,max_lst


def second(cur_x, cur_y, map_lst):
    max_cnt =0 
    max_lst=map_lst[:]
    for i in range(2):
        cnt=0
        map_lst_copy = copy.deepcopy(map_lst)
        for dir in range((i*2),(i*2)+2):
            queue = deque([(cur_x,cur_y)])
            dx,dy = d[dir][0],d[dir][1]
            while queue:
                x,y = queue.popleft()
                nx, ny = dx + x, dy + y
                if 0<=nx<h and 0<=ny<w:
                    if map_lst_copy[nx][ny]==6:
                        break
                    elif map_lst_copy[nx][ny]!=0:
                        queue.append((nx,ny))
                        continue
                    cnt+=1
                    map_lst_copy[nx][ny]="#"
                    queue.append((nx,ny))

        if cnt>max_cnt:
            max_cnt=cnt
            max_lst=map_lst_copy[:]
    return max_cnt,max_lst

def third(cur_x, cur_y, map_lst):
    max_cnt =0 
    max_lst=map_lst[:]
    for i in range(4):
        cnt=0
        map_lst_copy = copy.deepcopy(map_lst)
        for dir in [(i)%4,(i+1)%4]:
            queue = deque([(cur_x,cur_y)])
            dx,dy = d[dir][0],d[dir][1]
            while queue:
                x,y = queue.popleft()
                nx, ny = dx + x, dy + y
                if 0<=nx<h and 0<=ny<w:
                    if map_lst_copy[nx][ny]==6:
                        break
                    elif map_lst_copy[nx][ny]!=0:
                        queue.append((nx,ny))
                        continue
                    cnt+=1
                    map_lst_copy[nx][ny]="#"
                    queue.append((nx,ny))

        if cnt>max_cnt:
            max_cnt=cnt
            max_lst=map_lst_copy[:]
    return max_cnt,max_lst

def fourth(cur_x, cur_y, map_lst):
    max_cnt =0 
    max_lst=map_lst[:]
    for i in range(4):
        cnt=0
        map_lst_copy = copy.deepcopy(map_lst)
        arr = [i%4,(i+1)%4,(i+2)%4]
        for dir in arr:
            queue = deque([(cur_x,cur_y)])
            dx,dy = d[dir][0],d[dir][1]
            while queue:
                x,y = queue.popleft()
                nx, ny = dx + x, dy + y
                if 0<=nx<h and 0<=ny<w:
                    if map_lst_copy[nx][ny]==6:
                        break
                    elif map_lst_copy[nx][ny]!=0:
                        queue.append((nx,ny))
                        continue
                    cnt+=1
                    map_lst_copy[nx][ny]="#"
                    queue.append((nx,ny))

        if cnt>max_cnt:
            max_cnt=cnt
            max_lst=map_lst_copy[:]
    return max_cnt,max_lst



def fifth(cur_x,cur_y,map_lst):
    max_cnt =0 
    map_lst_copy = copy.deepcopy(map_lst)
    
    for dx, dy in d:
        queue = deque([(cur_x,cur_y)])
        while queue:
            x, y = queue.popleft()
            nx, ny = dx + x, dy + y
            if 0<=nx<h and 0<=ny<w:
                if map_lst_copy[nx][ny]==6:
                    break
                elif map_lst_copy[nx][ny]!=0:
                    queue.append((nx,ny))
                    continue
                max_cnt+=1
                map_lst_copy[nx][ny]="#"
                queue.append((nx,ny))
     
    return max_cnt,map_lst_copy


d=[(0,1),(0,-1),(1,0),(-1,0)]
h, w = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(h)]
total=0
res= h*w
pos_lst= []
for i in range(h):
    for j in range(w):
        if lst[i][j]==6:
            res-=1
            continue
        if lst[i][j]==1:
            pos_lst.append((1,i,j))
            res-=1
        elif lst[i][j]==2:
            pos_lst.append((2,i,j))
            res-=1
        elif lst[i][j]==3:
            pos_lst.append((3,i,j))
            res-=1
        elif lst[i][j]==4:
            pos_lst.append((4,i,j))
            res-=1
        elif lst[i][j]==5:
            pos_lst.append((5,i,j))
            res-=1

def dfs_per(lst,idx, t):
    if 

dfs_per([],0)
for num,pos_x,pos_y in pos_lst:
    if num == 1:
        cnt,lst=first(pos_x,pos_y,lst)
    elif num == 2:
        cnt,lst=second(pos_x,pos_y,lst)
    elif num == 3:
        cnt,lst=third(pos_x,pos_y,lst)
    elif num == 4:
        cnt,lst=fourth(pos_x,pos_y,lst)
    elif num == 5:
        cnt,lst=fifth(pos_x,pos_y,lst)
    total+=cnt

print(res-total)
