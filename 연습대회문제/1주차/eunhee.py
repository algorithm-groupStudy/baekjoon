
l,c=map(int,input().split())

def cnt_alpha(string):
    moum_cnt=0
    jaum_cnt=0
    moum=["a","e","i","o","u"]
    for s in string:
        if s in moum:
            moum_cnt+=1
        else:
            jaum_cnt+=1
    if moum_cnt>=1 and jaum_cnt>=2:
        return True
    return False

alpha_lst=list(map(str,input().split()))
alpha_lst.sort()
moum_cnt=0
jaum_cnt=0
res_lst=[]
for i in range(1,1<<c):
    string=""
    for j in range(c):
        if i& 1<<j:
            string+=alpha_lst[j]
    if len(string)==l:
        if cnt_alpha(string):
            res_lst.append(string)
res_lst.sort()
for i in res_lst:
    print(i)

