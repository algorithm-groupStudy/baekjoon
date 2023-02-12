# 다시 풀 것
import sys
sys.stdin = open("test.txt")


def check_sign(lst):
    mult = 1
    total = 0
    sign_lst = []
    for i in range(len(lst)):
        if lst[i] == "(":
            mult *= 2
            sign_lst.append("(")
        elif lst[i] == ")":
            if len(sign_lst) == 0 or sign_lst[-1] == "[":
                return 0
            sign_lst.pop()
            if lst[i-1] == "(":
                total += mult
            mult //= 2
        elif lst[i] == "[":
            mult *= 3
            sign_lst.append("[")
        elif lst[i] == "]":
            if len(sign_lst) == 0 or sign_lst[-1] == "(":
                return 0
            sign_lst.pop()
            if lst[i-1] == "[":
                total += mult
            mult //= 3
    if sign_lst:
        total = 0
    return total


lst = list(input())
total = check_sign(lst)

print(total)
