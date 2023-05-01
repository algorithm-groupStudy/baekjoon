N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if j<board[i][j]+j < N:
            dp[i][board[i][j]+j]+=dp[i][j]
            
        if i<board[i][j]+i < N:
            dp[board[i][j]+i][j]+=dp[i][j]
            
       
print(dp[-1][-1])    