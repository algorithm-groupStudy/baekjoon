import sys
sys.stdin = open("test.txt")

sign_lst = list(input())
stack = []
mult = 1
total=0
for i in range(len(sign_lst)):
    if sign_lst[i]=="(":
        mult*=2
        stack.append("(")
    elif sign_lst[i]==")":
        if not stack or stack[-1]=="[":
            total=0
            break
        stack.pop()
        if sign_lst[i-1]=="(":
            total+=mult
        mult//=2
    elif sign_lst[i]=="[":
        mult*=3
        stack.append("[")
    elif sign_lst[i]=="]":
        if not stack or stack[-1]=="(":
            total=0
            break
        stack.pop()
        if sign_lst[i-1]=="[":
            total+=mult
        mult//=3
if stack:
    total=0
print(total)