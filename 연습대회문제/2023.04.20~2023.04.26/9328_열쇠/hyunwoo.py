from collections import deque
import sys
sys.stdin = open('input.txt')

# 일단, 현재 위치에서 갈 수 있는 문서 정리
# 갈 수 있는 문서까지 가는 거리 중, 문이면 list에 넣기
# 문이 없으면 획득 += 1 
# 문이 있으면, 키 찾기, 키를 찾기 위한 키를 찾아야 한다면 해당 키부터 찾기 
# 

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    c = [[0]*(width+2) for _ in range(height+2)]
    q.append([x, y])
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height+2 and 0 <= ny < width+2:
                if not c[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])
                elif world[nx][ny].islower():
                    door[ord(world[nx][ny]) - ord('a')] = 1
                    q = deque()
                    c = [[0] * (width+2) for _ in range(height+2)]
                    world[nx][ny] = '.'
                    q.append([nx, ny])
                elif world[nx][ny].isupper():
                    if door[ord(world[nx][ny]) - ord('A')]:
                        c[nx][ny] = 1
                        door[nx][ny] = '.'
                        q.append([nx, ny])
                elif door[nx][ny] == '$':
                    c[nx][ny] = 1
                    cnt += 1
                    door[nx][ny] = '.'
                    q.append([nx, ny])
    print(cnt)
    

def new_map():
    for i in world:
        i.insert(0, '.')
        i.append('.')
    door.insert(0, ['.'] * (width + 2))
    door.append(['.'] * (width + 2))
        
                    
                    

t = int(input())
for test_case in range(1,t+1):
    height, width = map(int, input().split())
    world = [list(input().split()) for _ in range(height)]
    key_holding = list(input())
    door = [0] * 26
    
    for k in key_holding:
        if k != '0':
            door[ord(k)-ord('a')] = 1
    
    for i in range(height):
        for j in range(width):
            if ord('A') <= ord(world[i][j]) <= ord('Z'):
                if door[ord(world[i][j]) - ord('A')]:
                    world[i][j] = '.'
    new_map()
    bfs(0, 0)
    tc -= 1
            
    
    