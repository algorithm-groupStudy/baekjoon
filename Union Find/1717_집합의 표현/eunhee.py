# 다시보기
import sys
sys.setrecursionlimit(100000)
sys.stdin = open("test.txt")

def union(num1,num2):    # 합치기
    num1=find(num1)    # 합치기 전에 해당 노드의 부모를 찾아준다
    num2=find(num2)    # 합치기 전에 해당 노드의 부모를 찾아준다 22
    if num1==num2:    # 두 부모가 같으면 합칠 필요가 없음
        return
    parent[num1]=num2    # 숫자가 작은 노드 부모값에 숫자가 큰 노드 부모값 덮어 씌우기
    return 

def find(x):    # 부모노드 찾아주기
    if parent[x]==x:    # 부모노드가 자기 자신이면 계산할 필요가 없으므로 리턴
        return x
    parent[x]=find(parent[x])    # 자신의 조상님 찾아서 값 덮어씌어주기
    return parent[x]    # 조상님 반환
    
    

n,m=map(int,input().split())
parent=list(range(n+1))
for _ in range(m):
    action, a, b=map(int,input().split())
    if not action:    # action =0일때 합치기
        union(a,b)
    else:    
        # action = 1 일때 부모찾아서 부모 같으면 
        # 두 노드가 같은 집합안에 있는것이므로 yes, 아니면 no
        p_a = find(a)
        p_b = find(b)
        if p_a==p_b:
            print("yes")
        else:
            print("no")



#action: 0
# case: 0 1 3
# i: 0   [0, 3, 2, 3, 4, 5, 6, 7]

# NO
# action: 1
# case: 1 1 7
# i: 1   [0, 3, 2, 3, 4, 5, 6, 7]

# action: 0
# case: 0 7 6
# i: 2   [0, 3, 2, 3, 4, 5, 6, 6]

# NO
# action: 1
# case: 1 7 1
# i: 3   [0, 3, 2, 3, 4, 5, 6, 6]

# action: 0
# case: 0 3 7
# i: 4   [0, 3, 2, 6, 4, 5, 6, 6]

# action: 0
# case: 0 4 2
# i: 5   [0, 3, 2, 6, 2, 5, 6, 6]

# action: 0
# case: 0 1 1
# i: 6   [0, 6, 2, 6, 2, 5, 6, 6]

# YES
# action: 1
# case: 1 1 1
# i: 7   [0, 6, 2, 6, 2, 5, 6, 6]