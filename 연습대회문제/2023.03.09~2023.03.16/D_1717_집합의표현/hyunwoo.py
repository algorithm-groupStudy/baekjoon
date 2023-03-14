import sys
sys.stdin = open('/Users/hyunwoochoi/Desktop/python/algo/baekjoon/input.txt')

# m은 입력으로 주어지는 연산의 갯수 
n, m = map(int, input().split())

# 합집합 연산과 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산

subset = []
for idx in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:
        subset.append([a,b])
    elif operation == 1:
        if [a,b] in subset:
            print("YES")
        else:
            print("NO")
    


