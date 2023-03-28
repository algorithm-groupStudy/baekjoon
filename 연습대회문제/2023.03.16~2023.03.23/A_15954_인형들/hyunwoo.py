import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
dolls_love = list(map(float, input().split()))

ans = float('inf')

for M in range(K, N+1):
    ways = 1
    for i in range(1, M+1):
        ways *= (N-K+1-i+1) / i
    for i in range(N-M+1):
        avg = sum(dolls_love[i:i+M]) / M
        dsprs = sum([(d - avg)**2 for d in dolls_love[i:i+M]]) / M
        # 분산의 제곱근을 구합니다.
        result = dsprs ** 0.5
        # 최솟값을 갱신합니다.
        ans = min(ans, result)

print(ans)
