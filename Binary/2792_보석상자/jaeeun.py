import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
jewels = [int(input()) for _  in range(M)] 

def binary(target, arr, maxlen):
    l, r = 1, maxlen 
    result = maxlen
    while l <= r:
        mid = (l + r) // 2
        total = 0 
        for item in arr: 
            total += ((item // mid) + bool(item % mid))

        if total > target: 
            l = mid + 1 
        
        else: 
            result = min(mid, result) 
            r = mid - 1 
    
    return result 

print(binary(N, jewels, max(jewels)))
