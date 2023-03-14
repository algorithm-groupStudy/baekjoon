import sys
sys.stdin = open('/Users/hyunwoochoi/Desktop/python/algo/baekjoon/input.txt')

# N: number of words, K: time to teach

N, K = map(int, input().split())

words = []
for _ in range(N):
    tmp_word = list(input())
    words.append(len(tmp_word[4:-4]))

words.sort(key lambda=)

K -= 5 

while K > 0:
    if i > N-1 :
        break
    elif K >= words[i] :
        K -= words[i]
        i += 1 
    else:
        break 
print(i)