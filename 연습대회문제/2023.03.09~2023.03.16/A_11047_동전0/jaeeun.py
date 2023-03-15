# BOJ 11047 동전0

# 동전 N 종류, 가치의 합 K를 만든다.
# coins: N 개 동전의 가치
# 필요한 동전 개수의 최솟값 출력
# 조건: 동전의 가치 Ai는 오름차순으로 주어지며, 첫 번째 동전 A1은 가치 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수
# 조건을 보면 가장 가치가 높은 동전을 최대한 많이 사용하는 것이 조다.
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0
# 가치가 가장 큰 동전을 최대한 많이 사용.
for i in range(N-1, -1, -1):
    if K == 0:
        break
    count += K // coins[i]
    K = K % coins[i]


print(count)