L, C = map(int, input().split())
chars = sorted(input().split()) 
vowels = 'aeiou'

password = []
for i in range(1<<C):
    word = '' 
    for j in range(C):
        if i & (1<<j): 
            word += chars[j]
    if len(word) == L:
        v_count = 0 
        c_count = 0 
        for w in word:
            if w in vowels: 
                v_count += 1
            else:
                c_count += 1 
        if v_count >= 1 and c_count >= 2:
            password.append(word)
password.sort()
for p in password:
    print(p)

