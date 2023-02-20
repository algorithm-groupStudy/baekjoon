# BOJ 9012
# 괄호

T = int(input())
for tc in range(1, T + 1):
    paren = input()
    stack = []
    res = 'NO'
    for p in paren:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack:
                break
            else:
                stack.pop()
    else:
        if not stack:
            res = 'YES'

    print(res)