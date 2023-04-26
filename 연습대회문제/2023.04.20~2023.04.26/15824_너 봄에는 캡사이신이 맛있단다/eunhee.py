import sys
input = sys.stdin.readline
def pow(a,b):
    return a**b
# 5, 2, 8
N = int(input())
menu = list(map(int,input().split()))
menu.sort()

res=0

for i in range(N):
    res+=menu[i]*(pow(2,i) - pow(2, N-i-1))
# 경우의 수를 이용한 풀이

print(res%1000000007)