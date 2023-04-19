import sys
sys.stdin = open("test.txt")

lst = list(input())
stack=[]
total = 0
cal = 1
for i in range(len(lst)):
    if lst[i]=="(":
        cal*=2
        stack.append(lst[i])
    elif lst[i]==")":
        if not stack or (stack and stack[-1]=="["):
            total=0
            break
        stack.pop()
        if lst[i-1]=="(":
            total+=cal
        cal//=2
        
    elif lst[i]=="[":
        cal*=3
        stack.append(lst[i])

    elif lst[i]=="]":
        if not stack or (stack and stack[-1]=="("):
            total=0
            break
        stack.pop()
        if lst[i-1]=="[":
            total+=cal
        cal//=3
if stack:
    total=0
print(total)