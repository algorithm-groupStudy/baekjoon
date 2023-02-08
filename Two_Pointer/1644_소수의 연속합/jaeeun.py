N = int(input())
prime = []

# 범위 내 소수 구하는 법: 에라토스테네스의 체 참고 
import math 

num_list = [True for i in range(N+1)]
num_list[0] = False 
num_list[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if num_list[i]:
        j = 2 
        while i * j <= N: 
            num_list[i * j] = False 
            j += 1 

prime = [idx for idx, v in enumerate(num_list) if v]


length = len(prime)
end = 0 
count = 0
prime_sum = 0 

for start in range(length):
    while prime_sum < N and end < length:
        prime_sum += prime[end]
        end += 1 
    if prime_sum == N: 
        count += 1 
    prime_sum -= prime[start]


print(count)