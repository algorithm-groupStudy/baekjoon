import sys
sys.stdin = open('input.txt')

# def dfs(lst,x,y,position):
#     global count 
#     # 목적지에 도착하면 리턴 
#     if len(lst) == x == y:
#         count += 1 
#         return
    
#     if position == 0 or position == 2:  # 가로로 갈 수 있는 경우
#         if y + 1 < len(lst) and lst[x][y + 1] == 0:
#             dfs(lst, x, y + 1, 0)
#     if position == 1 or position == 2:  # 세로로 갈 수 있는 경우
#         if x + 1 < len(lst) and lst[x + 1][y] == 0:
#             dfs(lst, x + 1, y, 1)
#     if x + 1 < len(lst) and y + 1 < len(lst):
#         if lst[x + 1][y + 1] == 0 and lst[x + 1][y] == 0 and lst[x][y + 1] == 0:  # 대각선
#             dfs(lst, x + 1, y + 1, 2)
    
#     return 

def pipe(x, y, location):
    global ans
    if x == n - 1 and y == n - 1:  # 도착
        ans += 1
        return
    if location == 0 or location == 2:  # 가로로 갈 수 있는 경우
        if y + 1 < n and board[x][y + 1] == 0:
            pipe(x, y + 1, 0)
    if location == 1 or location == 2:  # 세로로 갈 수 있는 경우
        if x + 1 < n and board[x + 1][y] == 0:
            pipe(x + 1, y, 1)
    if x + 1 < n and y + 1 < n:
        if board[x + 1][y + 1] == 0 and board[x + 1][y] == 0 and board[x][y + 1] == 0:  # 대각선
            pipe(x + 1, y + 1, 2)


# size_of_map = int(input())
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
visited = []
pipe(0,1,0)

print()

