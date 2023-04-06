# BOJ 1644 소수의 연속합

def find_sum(arr):
    l = -1
    r = -1
    cnt = 0
    total = 0
    while True:
        if total == N:
            cnt += 1
        if total <= N:
            r += 1
            if r >= len(arr):
                break
            total += arr[r]
        else:
            l += 1
            total -= arr[l]
    return cnt


N = int(input())

# (소수 구하기) 아래 부분을 에라토스테네스의 체를 사용할 수 있다.
prime = [1 for _ in range(N+1)]
prime[0] = 0
prime[1] = 0

for idx in range(N+1):
    if prime[idx] == 1:
        k = 2
        while idx * k < N + 1:
            prime[idx * k] = 0
            k += 1

prime_num = [k for k in range(N+1) if prime[k] == 1]

####### 에라토스테네스의 체
# num_list = [True for i in range(N+1)]
# num_list[0] = False
# num_list[1] = False
#
# for i in range(2, int(math.sqrt(N)) + 1):
#     if num_list[i]:
#         j = 2
#         while i * j <= N:
#             num_list[i * j] = False
#             j += 1
#
# prime = [idx for idx, v in enumerate(num_list) if v]
#######



print(find_sum(prime_num))