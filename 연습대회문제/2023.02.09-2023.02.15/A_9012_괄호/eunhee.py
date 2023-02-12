# import sys
# sys.stdin = open("test.txt")


def check_sign(lst):
    open = 0
    for sign in lst:
        if sign == "(":
            open += 1
        else:
            open -= 1
        if open < 0:
            open = 1  # ")"기호가 먼저 나왔을 경우, 값 1을 주고 반복문 탈출
            break
    return "NO" if open else "YES" 


t = int(input())
for i in range(t):
    lst = list(input())
    print(check_sign(lst))
