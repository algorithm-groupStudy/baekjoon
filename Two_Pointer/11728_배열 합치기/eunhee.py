import sys
sys.stdin=open("test.txt")
n,m=map(int,input().split())
lst=list(map(int,input().split()))+list(map(int,input().split()))

r=0
for l in range(len(lst)):
    while l<=r and r<len(lst):    
        if lst[l]>lst[r]:
            lst[l],lst[r]=lst[r],lst[l]
        r+=1
    
  
print(lst)