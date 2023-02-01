N, K = map(int,input().split())

dp = [0 for _ in range(N)]
kg = []
val = []

for i in range(N):
    a, b = map(int,input().split())
    kg.append(a)
    val.append(b)

for i in range(N):
    sum_kg=0
    while sum_kg<=dp[i]:
        
        pass