import sys
sys.stdin = open('input.txt')

# find next great element 
        
num_ele = int(input())
elements = list(map(int, input().split()))
ans = [-1] * num_ele # 초기 값을 전부 1로 설정 
stack = [0] # 첫 인덱스 0 
for i in range(1,num_ele):
    # 스텍이 존재하고
    # elements[i]가 elements[그전의 append된 순서] 보다 클때 
    while stack and elements[stack[-1]] < elements[i]:
        # 정답인덱스를 해당 수로 바꿔줌 
        ans[stack.pop()] = elements[i]  # 
    stack.append(i)  # i : 1,2,3,4,5 ~ num_ele 
    
print(*ans)
        