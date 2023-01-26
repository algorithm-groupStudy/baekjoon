from sys import stdin
from collections import defaultdict


def input():
    return stdin.readline().rstrip()

N, d, k, c = map(int, input().split())

#N: 벨트 위 접시 수, d: 초밥 총 가짓수, k: 연속 k개 먹기, c: 쿠폰 번호

sushis = [int(input()) for _ in range(N)]
plates = defaultdict(int)
plates[c] = 1

cnt = 1
for i in range(k):
    if plates[sushis[i]] == 0:
        cnt += 1
    plates[sushis[i]] += 1

res = cnt
for end in range(k, N + k - 1):
    plates[sushis[end - k]] -= 1
    if plates[sushis[end - k]] == 0:
        cnt -= 1

    plates[sushis[end % N]] += 1
    if plates[sushis[end % N]] == 1:
        cnt += 1

    res = max(cnt, res)

print(res)


''' (풀이코드)
table = [int(input()) for i in range(N)]
table.extend(table[:k-1])

from collections import defaultdict

sushi_type = defaultdict(int)

for t in table[:k]:
    sushi_type[t] += 1 
    sushi_count = 0
    for s in sushi_type.values():
        if s != 0: 
            sushi_count += 1 
   
if sushi_type[c] == 0:
    sushi_count += 1


for start in range(0, N-1):
    sushi_type[table[start]] -= 1 
    sushi_type[table[start+k]] += 1 
    curr_len = 0
    for s in sushi_type.values():
        if s != 0: 
            curr_len += 1
    if sushi_type[c] == 0:
        curr_len += 1 
    sushi_count = max(sushi_count, curr_len)


print(sushi_count)

'''