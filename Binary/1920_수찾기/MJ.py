# 자료 구조를 이용한 풀이

import sys
input = sys.stdin.readline

# 자료형 이용
N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)
