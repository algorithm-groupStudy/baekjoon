import time as t

s1=t.time()

for i in range(100000000):
    a=i

e1=t.time()

print(e1-s1,"초 걸림")

lst2=list(range(100000000))
s2=t.time()

for i in lst2:
    a=i

e2=t.time()

print(e2-s2,"초 걸림")

print("끝")