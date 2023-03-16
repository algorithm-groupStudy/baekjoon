import sys
import itertools
input = sys.stdin.readline

N, K = map(int, input().split())
words = set(input().strip() for _ in range(N))

if K < 5:
    print(0)
else:
    base = 0
    for c in ('a', 'c', 'i', 'n', 't'):
        base |= (1 << (ord(c) - ord('a')))

    maxCntReadable = -1
    for comb in itertools.combinations(range(26), K-5):
        mask = base
        for i in comb:
            mask |= (1 << i)
        cntReadable = 0
        for word in words:
            isReadable = True
            for c in word:
                if not (mask & (1 << (ord(c) - ord('a')))):
                    isReadable = False
                    break
            if isReadable:
                cntReadable += 1
        maxCntReadable = max(maxCntReadable, cntReadable)
    print(maxCntReadable)