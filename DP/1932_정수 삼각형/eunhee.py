n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
t_arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    t_arr[i][:i+1] = map(int, input().split())

arr[0][0] = t_arr[0][0]
for i in range(n-1):
    for j in range(i+1):
        arr[i+1][j] = max(arr[i+1][j], arr[i][j]+t_arr[i+1][j])
        arr[i+1][j+1] = max(arr[i+1][j+1], arr[i][j]+t_arr[i+1][j+1])
print(max(arr[-1]))
