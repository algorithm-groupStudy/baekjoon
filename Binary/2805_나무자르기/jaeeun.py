N, M = map(int, input().split())
trees = list(map(int, input().split()))

def binary(target, arr, max_height):
    l, r = 0, max_height
    while l <= r: 
        mid = (l + r) // 2
        wood = 0 
        for item in arr:
            if item > mid:
                wood += item - mid
        if wood == target: 
            return mid 
        elif wood < target:
            r = mid - 1 
        else:
            result = mid 
            l = mid + 1
    return result 


print(binary(M, trees, max(trees)))