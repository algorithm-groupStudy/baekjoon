def check(hp_arr):
    global res
    cnt = 0
    for hp in hp_arr:
        if hp <= 0:
            cnt += 1
    res = max(res, cnt)


def dfs(idx):
    global eggs, hp_arr, weight_arr, visited
    if idx == eggs:
        check(hp_arr)
        return
    if hp_arr[idx] > 0:
        crack_egg = True
        for i in range(eggs):
            if hp_arr[i] > 0 and i != idx:
                crack_egg = False
                hp_arr[i] -= weight_arr[idx]
                hp_arr[idx] -= weight_arr[i]
                dfs(idx+1)
                hp_arr[i] += weight_arr[idx]
                hp_arr[idx] += weight_arr[i]
        if crack_egg:
            # 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란 and 깨지지 않은 계란이 없는 상태일 경우
            check(hp_arr)
            return
    else:
        dfs(idx+1)


eggs = int(input())
hp_arr = []
weight_arr = []
visited = [False for _ in range(eggs)]
res = 0
for i in range(eggs):
    hp, weight = map(int, input().split())
    hp_arr.append(hp)
    weight_arr.append(weight)

dfs(0)
print(res)
