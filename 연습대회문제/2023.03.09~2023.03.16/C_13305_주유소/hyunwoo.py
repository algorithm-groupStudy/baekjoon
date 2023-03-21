num_city = int(input())
dis_city = list(map(int, input().split()))
oil_city = list(map(int, input().split()))

# 시작 도시 
oil_price = oil_city[0]
total = 0
for i in range(num_city-1):
    if oil_price > oil_city[i]:
        oil_price = oil_city[i]
    total += oil_price * dis_city[i]

print(total)
