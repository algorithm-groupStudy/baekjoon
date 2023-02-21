import sys
sys.stdin = open("text.txt")

# n = int(input())
# lst = list(map(int, input().split()))+[-1]
# stack = []
# for i in range(n):
#     idx = i
#     stack.append(lst[i])

#     while stack and idx < n and stack[-1] >= lst[idx]:
#         idx += 1

#     if stack and stack[-1] < lst[idx]:
#         stack.pop()
#         stack.append(lst[idx])
#         continue
#     stack.pop()
#     stack.append(lst[idx])
# print(*stack)


# n = int(input())
# A = list(map(int, sys.stdin.readline().split()))
# answer = [-1] * n
# stack = []


# stack.append(0)
# for i in range(1, n):
#     while stack and A[stack[-1]] < A[i]:
#         answer[stack.pop()] = A[i]
#     stack.append(i)


# print(*answer)
