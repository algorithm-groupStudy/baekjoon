import sys
sys.setrecursionlimit(10**5)

getInt = lambda: int(sys.stdin.readline())
getStr = lambda: sys.stdin.readline().rstrip()
getInts = lambda: list(map(int, sys.stdin.readline().split()))

N = getInt()
orders = [getStr().split() for _ in range(N)]

"""
in_cnt: 해당 word 앞에 와야하는데 아직 등장하지 않은 word의 개수
to_list: 해당 word 뒤에 등장하는 word 리스트 (graph라고 보면 된다)

기본 아이디어:
처음에 to_list(graph)를 만든 다음에 in_cnt를 추가로 만들어준다.
in_cnt가 0인 word들만 백남이가 구매할 수 있다.
in_cnt가 0인 word들을 모두 뽑아서 정렬해서 모은 다음에, 해당 word들 다음에 나오는 word들의 in_cnt를 감소시켜준다. 이걸 반복한다.

왜 중요한 문제인가:
위상정렬이라는 알고리즘 문제인데 위상정렬 아닌 척 만든 문제다. 위상정렬 문제를 풀 때 in_cnt를 유지/업데이트하는 기법을 자주 쓰게 된다.
"""
in_cnt = {}
to_list = {}

for l, r in orders:
  if not l in in_cnt:
    in_cnt[l] = 0
  if not r in in_cnt:
    in_cnt[r] = 0
  in_cnt[r] += 1

  if not l in to_list:
    to_list[l] = []
  to_list[l].append(r)
  if not r in to_list:
    to_list[r] = []

cands = []
result = []

for k, v in in_cnt.items():
  if v == 0:
    cands.append(k)

while len(cands) > 0:
  cands.sort()
  new_cands = []

  for c in cands:
    result.append(c)
    for to in to_list[c]:
      in_cnt[to] -= 1
      if in_cnt[to] == 0:
        new_cands.append(to)
  cands = new_cands

if len(result) == len(to_list):
  print('\n'.join(result))
else:
  print(-1)
