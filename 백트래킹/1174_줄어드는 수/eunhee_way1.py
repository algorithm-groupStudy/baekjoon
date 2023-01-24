n = int(input())


def dfs(num):
    global res
    res.append(int(num))
    for i in range(0, int(num[-1])):
        dfs(num+str(i))


res = []
for i in range(10):
    dfs(str(i))
if n-1 >= len(res):
    print(-1)
else:
    res.sort()
    print(res[n-1])
print("res:", res)
