n, k = map(int, input().split())
string = list(input())
stack = []
for num in string:
    while stack and int(num) > int(stack[-1]) and k > 0:
        stack.pop()
        k -= 1
    stack.append(num)

if k > 0:
    print("".join(stack[:-k]))
else:
    print("".join(stack))
