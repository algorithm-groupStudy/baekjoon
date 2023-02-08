N, K = map(int, input().split())
temps = list(map(int, input().split()))

max_temp = sum(temps[:K])
curr_temp = max_temp
for start in range(N-K):
    curr_temp += temps[start+K] - temps[start]
    if curr_temp > max_temp: 
        max_temp = curr_temp

print(max_temp)
