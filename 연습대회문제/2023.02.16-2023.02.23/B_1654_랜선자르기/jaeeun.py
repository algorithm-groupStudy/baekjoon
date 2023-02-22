def binary(length, goal):
    l = 1
    r = max(length)  # 처음에 min으로 해서 틀렸다 
    res = 0
    while l <= r:
        mid = (l + r) // 2
        total = 0
        for line in length:
            total += line // mid
        if total < goal:
            r = mid - 1
        else:
            res = mid
            l = mid + 1

    return res


K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]
res = binary(length, N)

print(res)

