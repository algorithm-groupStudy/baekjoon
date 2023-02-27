import sys
sys.stdin = open("test.txt")
input = sys.stdin.readline
n = int(input())
milk_store = [list(map(int, input().split())) for _ in range(n)]
d = [(-1, 0), (0, -1)]
dp = [[[0, -1] for _ in range(n+1)] for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, n+1):
        l, u = dp[i][j-1], dp[i-1][j]
        l_cnt = l[0]+1 if (l[1]+1) % 3 == milk_store[i-1][j-1] else l[0]
        u_cnt = u[0]+1 if (u[1]+1) % 3 == milk_store[i-1][j-1] else u[0]

        if l_cnt > u_cnt:
            dp[i][j][0] = l_cnt
            dp[i][j][1] = milk_store[i-1][j -
                                          1] if (l[1]+1) % 3 == milk_store[i-1][j-1] else l[1]
        else:
            dp[i][j][0] = u_cnt
            dp[i][j][1] = milk_store[i-1][j -
                                          1] if (u[1]+1) % 3 == milk_store[i-1][j-1] else u[1]


# 아래 코드는 왜 틀렸을까??
            # for dx, dy in d:
            #     nx, ny = i+dx, j+dy
            #     if (dp[nx][ny][1]+1) % 3 == milk_store[i-1][j-1]:
            #         dp[i][j][0] = max(dp[nx][ny][0]+1, dp[i][j][0])
            #         dp[i][j][1] = milk_store[i-1][j-1]
            #     else:
            #         dp[i][j][0] = max(dp[nx][ny][0], dp[i][j][0])
            #         dp[i][j][1] = dp[nx][ny][1] if dp[nx][ny][0] >= dp[i][j][0] else dp[i][j][1]

print(dp[n][n][0])
