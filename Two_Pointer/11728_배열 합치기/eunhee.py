import sys
sys.stdin=open("test.txt")
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
lst=[]

p1,p2=0,0
while p1<n and p2<m:
    

# print("lst:",lst)
# # for l in range(len(lst)-1):
# #     r=l+1
# #     while r<len(lst):  
# #         if lst[l]>lst[r]:
# #             lst[l],lst[r]=lst[r],lst[l]  
# #         r+=1

# l=0
# r=l+1
# # while r<len(lst):  
# #     if lst[l]>lst[r]:
# #         lst[l],lst[r]=lst[r],lst[l]  
# #         r+=1
    
  
print(*lst)