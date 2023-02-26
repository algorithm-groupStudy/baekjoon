import sys
sys.stdin = open("test.txt")
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, -1] for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        left, up = dp[i][j-1], dp[i-1][j]
        left_check = (left[1]+1) % 3 == mat[i-1][j-1]
        up_check = (up[1]+1) % 3 == mat[i-1][j-1]

        left_score = left[0] + left_check
        up_score = up[0] + up_check
        if left_score > up_score:
            dp[i][j][0] = left_score
            dp[i][j][1] = mat[i-1][j-1] if left_check else left[1]

        else:
            dp[i][j][0] = up_score
            dp[i][j][1] = mat[i-1][j-1] if up_check else up[1]
for row in dp:
    print(row)
print(dp[N][N][0])
