N = int(input())
arr = list(map(int,input().split()))
stack = []
count = [0]*len(arr)

for i in range(len(arr)):
    while stack!=[]:
        if arr[i]<arr[stack[-1]]:   # stack[-1]  인덱스값임 
            count[i]=stack[-1]+1
            break
        else:
            stack.pop()

    stack.append(i)
print(*count)