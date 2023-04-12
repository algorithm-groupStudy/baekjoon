#  N: number of trees, M: needs tree length
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# define returns when cut
def cut(arr, height):
    total_cut = 0
    for tree in arr:
        if tree - height > 0:
            total_cut += tree-height
    return total_cut


# binary search?
start = 0
end = max(trees)

while end >= start:
    mid = (start + end) // 2

    if cut(trees,mid) >= M:
        start = mid + 1
    else:
        end = mid - 1

print(start-1)