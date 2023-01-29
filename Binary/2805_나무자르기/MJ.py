# 나무 자르기
# 149776 KB	 4256 ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Woods = list(map(int, input().split()))

left, right= 1, max(Woods)
while left <= right:
    mid = (left + right) // 2
    res = 0         # 잘린 나무 길이 합
    for wood in Woods:
        if wood > mid:
            res += wood - mid
    #res = sum(Woods[mid:]) - Woods[mid] * len(Woods[mid:])
    if res < M:             # case 1, 오른쪽 땡길 때
        right = mid - 1
    else:        #(res >= M)
        left = mid + 1
print(right)
