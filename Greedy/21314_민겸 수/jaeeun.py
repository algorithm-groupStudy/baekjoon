# BOJ 21314
# 민겸 수

num = input()

k_idx = []
for idx, n in enumerate(num):
    if n == 'K':
        k_idx.append(idx)


length = len(num)
start = 0
max_str = ''
min_str = ''

if len(k_idx) == 0:
    max_str = '1' * length
    min_str = '1' + '0' * (length - 1)

else:
    for k in k_idx:
        max_str += ('5' + (k - start) * '0')

        if k - start - 1 >= 0:
            min_str += ('1' + (k - start - 1) * '0') + '5'
        else:
            min_str += '5'

        start = k + 1

    if length-1 > k_idx[-1]:
        max_str += '1' * (length-1-k_idx[-1])
        min_str += '1' + '0' * (length-2-k_idx[-1])

print(max_str)
print(min_str)