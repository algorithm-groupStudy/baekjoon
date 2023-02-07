n = int(input())
 
data = [] 
rank = [] 
for i in range(n):
    weight, height = map(int, input().split())
    data.append((weight, height)) 
    
for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
            count += 1 
    rank.append(count + 1) # 덩치 등수는 자신보다 몸무계 키 모두 큰 사람의 수 + 1 이므로 count + 1을 rank에 append한다.

print(*rank)