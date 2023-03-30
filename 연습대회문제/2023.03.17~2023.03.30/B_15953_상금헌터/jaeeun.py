# BOJ 15953 상금헌터

import sys

T = int(input())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())

    if a == 0:
        prize1 = 0
    elif a == 1:
        prize1 = 500
    elif 2 <= a < 4:
        prize1 = 300
    elif 4 <= a < 7:
        prize1 = 200
    elif 7 <= a < 11:
        prize1 = 50
    elif 11 <= a < 16:
        prize1 = 30
    elif 16 <= a < 22:
        prize1 = 10
    else:
        prize1 = 0

    if b == 0:
        prize2 = 0
    elif b == 1:
        prize2 = 512
    elif 2 <= b < 4:
        prize2 = 256
    elif 4 <= b < 8:
        prize2 = 128
    elif 8 <= b < 16:
        prize2 = 64
    elif 16 <= b < 32:
        prize2 = 32
    else:
        prize2 = 0

    res = (prize1+prize2) * 10000

    print(res)