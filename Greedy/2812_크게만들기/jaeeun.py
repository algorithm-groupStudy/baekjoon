# BOJ 2812
# 크게 만들기 
# 코드 참조 

N, K = map(int, input().split())
num = list(input())

k, stack = K, [] 
for idx in range(N): 
    while k > 0 and stack and stack[-1] < num[idx]:
        stack.pop()
        k -= 1
    stack.append(num[idx])


print(''.join(stack[:N-K]))

# K만큼 pop해주면 된다. 
# while 문 돌면서 K 값이 변경되므로 따로 복사해주서야 한다 (혹은 출력을 다른 방식으로)
