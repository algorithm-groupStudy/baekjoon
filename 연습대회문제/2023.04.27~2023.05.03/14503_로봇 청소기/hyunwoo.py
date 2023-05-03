import sys
sys.stdin = open('input.txt')

# 방의 상태가 주어졌을때, 청소하는 영역의 갯수를 구해라

# 방의 크기 
N, M = map(int,input().split())

# 로봇 청소기가 있는 점의 좌표, 바라보고 있는 방향 
x, y, way = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(M)]
result = 0
# 청소기 작동,
direction = [(0,1), (1,0), (0,-1), (-1,0)] # 북(0) 동(1) 남(2) 서(3) 

# 1. 현재 칸이 청소 되지 않은 경우, 현재 칸을 청소
def clean(x, y, room):
    global result 
    
    if room[x][y] == 1:
        room[x][y] = 0 
        result += 1
    else:
        # 2. 현재 칸의 주변 3칸 중 청소되지 않은 빈칸이 없는 경우, 후진 
        for i in range(3, -1, -1):
            
            # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는 경우.
            # 반시계 90도 회전, 바라보는 방향을 기준으로, 앞쪽 칸이 청소되지 않은 경우 한칸 전진
            # 1번으로 돌아간다. 
            
            
            
    