kind_coin, sum_coin = map(int,input().split())
coin_list =[]
cnt = 0
tmp_sum = sum_coin

for coin in range(kind_coin):
    coin_list.append(int(input()))

for i in range(len(coin_list)-1, -1, -1):
    tmp = 0
    if tmp_sum == 0:
        break
    elif tmp_sum >= coin_list[i]:
        tmp += tmp_sum // coin_list[i]
        tmp_sum -= coin_list[i] * tmp
        cnt += tmp

print(cnt)