import sys
sys.stdin = open("input.txt")
# 풀이 참조 하였음. 

n, k = map(int, input().split())
numbers = input().rstrip()
stack = []

# stack에 number를 넣고 새로운 number와 비교 후 가장 큰 숫자를 앞쪽에 위치하도록 numbers의 항목에서, k의 갯수 만큼 뺀 후 
for number in numbers:
    # stack에 뭐가 잇는 동안, stack [-1]이 각 넘버보다 작고, K가 0보다 클때 
    while stack and stack[-1] < number and k > 0:
        # stack에서 하나를 pop하고 
        stack.pop()
        # k를 빼고
        k -= 1
    # stack에 number를 append 
    stack.append(number)
    # k가 양수일때 
if k > 0:
    print(''.join(stack[:-k]))
else:  # K가 음수일때 
    print(''.join(stack))