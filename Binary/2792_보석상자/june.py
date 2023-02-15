N, M = map(int,input().split())
arr =[]
for i in range(M):
    bosuk = int(input())
    arr.append(bosuk)

    min_envy, max_envy = 1, max[arr]
    mid = (min_envy + max_envy)//2
    if mid<N:
        min_envy = mid +1
    elif mid>N:
        max_envy = mid-1