N = int(input())

students = []
table = [[] for _ in range(N*N+1)]

for _ in range(N*N): 
    stu, *friends = map(int, input().split())
    students.append(stu)
    table[stu] = friends

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [[0 for _ in range(N)] for _ in range(N)]

for stu in students:
    max_fr = []
    for x in range(N):
        for y in range(N):
            if graph[x][y] == 0:
                fr = 0 
                zero = 0 
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N: 
                        if graph[nx][ny] in table[stu]: 
                            fr += 1 
                        elif graph[nx][ny] == 0: 
                            zero += 1
                max_fr.append((fr, zero, x, y))
    max_fr.sort(key=lambda x: (-x[0], -x[1]))
    graph[max_fr[0][2]][max_fr[0][3]] = stu 

satisfaction = 0
for n in range(N):
    for m in range(N):
        count = 0 
        stu = graph[n][m]
        for k in range(4):
            nn = n + dx[k]
            nm = m + dy[k]
            if 0 <= nn < N and 0 <= nm < N:
                if graph[nn][nm] in table[stu]:
                    count += 1 
        if count == 4: 
            satisfaction += 1000
        elif count == 3:
            satisfaction += 100 
        elif count == 2: 
            satisfaction += 10 
        elif count == 1:
            satisfaction += 1

print(satisfaction)
        

    
    

    

                
                 
        



    

