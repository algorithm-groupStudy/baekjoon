num_line, need_line = map(int, input().split())
lines = []
for _ in range(num_line):
    lines.append(int(input()))

start , end = 1 , max(lines)

while start <= end:
    mid  = (start+end) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid
    if cnt >= need_line :
        start = mid + 1
    else:
        end = mid - 1
print(end)

