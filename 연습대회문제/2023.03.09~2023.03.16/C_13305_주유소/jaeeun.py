# BOJ 13305 주유소
# 각 길마다 지금까지 지난 주유소 중 가장 값이 싼 곳에서 기름을 채울 수 있도록 한다
N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_price = 1000000000
total = 0
for idx in range(N-1):
    if oil[idx] < min_price:
        min_price = oil[idx]
    total += road[idx] * min_price

print(total)