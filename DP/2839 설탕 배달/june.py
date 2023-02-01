N = int(input())
answer =-1
ex = 0
for i in range(0,N//3+1):
    for j in range(0,N+1-3*i,5):
        if 3*i+j==N:
            answer = i+int(j/5)
            ex = 1
            break
    if ex==1:
        break    
print(answer)

