import sys
sys.stdin = open("text.txt")

k, n = map(int, input().split())
lst = []
for i in range(k):
    line = int(input())
    lst.append(line)


def check(d):
    cnt = 0
    for i in lst:
        cnt += i//d
    return cnt


s = 1
e = max(lst)
cnt_r = 0
while s <= e:
    cnt_r += 1
    mid = (s+e)//2
    if check(mid) >= n:
        s = mid+1
    else:
        e = mid-1
print(e)
