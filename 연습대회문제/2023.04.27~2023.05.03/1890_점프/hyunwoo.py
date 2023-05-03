import sys
sys.stdin = open('input.txt')

board_size = int(input())

board = [list(map(int, input().split())) for  _ in range(board_size)]
result = 0 

# def dfs():
#     global result
#     queue = [(0,0)]
#     # 시작은 왼쪽 위에 (0,0) 도착은 (3,3)
    
#     while queue:
#         # 도착했다면, result 값 += 1 
        
#         start_x, start_y = queue.pop()
#         if start_x == 3 and start_y == 3:
#             reuslt += 1
#         power = board[start_x][start_y]
        
#         # 오른쪽, 왼쪽 확인 갈 수 있다면 queue에 넣어주기 
#         if board[start_x+power][start_y]:
#             queue.append((start_x+power,start_y))
#         if board[start_x][start_y+power]:
#             queue.append((start_x,start_y+power))

# dfs로 하면 시간초과

dp = [[0] * board_size for _ in range(board_size)]
dp[0][0] = 1

for i in range(board_size):
    for j in range(board_size):
        if i == (board_size -1) and j == (board_size - 1):
            print(dp[i][j])
            break
        power = board[i][j]
        # 오른쪽 가기
        if j + power < board_size:
            dp[i][j + power] += dp[i][j]
        if i + power < board_size:
            dp[i+ power][j] += dp[i][j]