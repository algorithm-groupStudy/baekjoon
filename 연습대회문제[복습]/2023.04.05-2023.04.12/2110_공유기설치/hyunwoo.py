import sys
input = sys.stdin.readline
num_house, num_router = map(int,input().split())
loc_house = []
for _ in range(num_house):
    loc_house.append(int(input()))

loc_house.sort()

start = 1
end = loc_house[-1] - loc_house[0]
result = 0

while (start <= end):
    mid = (start+end) // 2
    old = loc_house[0]
    count = 1

    for i in range(1, len(loc_house)):
        if loc_house[i] >= old + mid:
            count += 1
            old = loc_house[i]
    if count >= num_router:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)