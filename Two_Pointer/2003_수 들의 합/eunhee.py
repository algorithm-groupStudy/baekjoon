import sys
sys.stdin=open("test.txt")
n,m=map(int,input().split())
lst=list(map(int,input().split()))

# https://butter-shower.tistory.com/226 참고하면 좋을 블로그

def result(n,m,lst):
    cnt=0
    l,r=0,0
    total=0
    for i in range(n):
        l=i
        while total<m and r<n:    
            # total이 타깃보다 작고,
            # right포인트가 n보다 작을때
            # total보다 같거나 커질때까지 r을 계속 크게 만들음.
            total+=lst[r]
            r+=1
        if total==m:   # 같을경우 cnt+=1
            cnt+=1
        total-=lst[l]   # total에서 시작점 값을 빼고 옮기기.
    print(cnt)

result(n,m,lst)
