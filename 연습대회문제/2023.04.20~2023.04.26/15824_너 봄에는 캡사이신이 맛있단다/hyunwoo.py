import sys
sys.stdin = open('input.txt')

# number_of_menu = int(input())

# menu = list(map(int, input().split()))

# pain = 0

# from itertools import combinations

# for i in range(2, number_of_menu+1):
#     for combination in combinations(menu,i):
#         pain += max(combination) - min(combination)

# print(pain%1000000007)


# menu 정렬 후 왼쪽 끝, 오른쪽 끝이 포함되는 갯수 만큼 곱하기 
# 그다음 숫자 

# import sys

# number_of_menu = int(input())

# menu = list(map(int, input().split()))

# pain = 0

# # Precompute prefix sum array
# prefix_sum = [0]
# for item in menu:
#     prefix_sum.append(prefix_sum[-1] + item)

# # Use sliding window approach and avoid duplicate combinations
# for i in range(1, len(menu)):
#     for j in range(len(menu) - i):
#         if menu[j] < menu[j+i]:
#             subarray_sum = prefix_sum[j+i] - prefix_sum[j]
#             subarray_min = menu[j]
#             subarray_max = menu[j+i]
#             subarray_pain = subarray_max - subarray_min - (i-1) * subarray_min
#             pain = (pain + subarray_pain) % 1000000007

# print(pain)

# import sys
# input = sys.stdin.readline
# mod = 1000000007
# # 5, 2, 8
# N = int(input())
# menu = list(map(int,input().split()))
# menu.sort()

# res=0

# for i in range(N):
#     res += menu[i]*((1<<i) - (1<<N-i-1))
#     res %= mod 
# # 경우의 수를 이용한 풀이

# print(res)

import sys

N = int(sys.stdin.readline())
datas = sorted(list(map(int, sys.stdin.readline().split())))

MOD = 1000000007
res = 0
mul = 1
for i in range(1,N):
    res += ((datas[i]-datas[-i-1])%MOD)*mul%MOD
    res %= MOD
    mul = ((mul+1)*2-1 )%MOD

print(res)
