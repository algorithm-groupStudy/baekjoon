N = int(input())
request = list(map(int, input().split()))
M = int(input())

max_req = max(request)
if sum(request) <= M:
    print(max_req)

else: 
    l, r = 0, max_req
    found = False 
    while l <= r: 
        mid = (l + r) // 2
        total = 0 
        for req in request:
            total += min(mid, req) 
        if total == M: 
            print(mid)
            found = True
            break 
        elif total > M:
            r = mid - 1 
        else:
            result = mid 
            l = mid + 1 
    if not found: 
        print(result)

    # 코드 참고 후 수정: 총 예산액보다 작거나 같은 값을 찾기 위해 예산액보다 작은 경우를 result에 따로 저장 