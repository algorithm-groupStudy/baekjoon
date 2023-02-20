
def switch_status_m(num): #성별이 남자일때, 남자가 고른 숫자의 배수만 바꿔줌
    global switch_lst,n
    for i in range(1,(n//num)+1):
        switch_status=switch_lst[(i*num)-1] # 문제는 1부터 시작이지만, 배열 인덱스는 0부터 시작이므로 -1을 해줌
        switch_lst[(i*num)-1]=(switch_status+1)%2 # 0이면 1로, 1이면 0으로 바꿔줌
    

def switch_status_w(num): # 성별이 여자일때, 여자가 고른 숫자의 좌우대칭을 체크.
    global switch_lst,n
    check_switch_cnt=min(n-num,num-1) # 좌우 대칭 체크 수 구하기, 배열 범위를 넘으면 안되므로, 최솟값으로 설정
    min_idx=num-1
    max_idx=num-1
    for i in range(1,check_switch_cnt+1):
        if switch_lst[num-1+i]==switch_lst[num-1-i]: # 좌우대칭 체크
            min_idx=num-1-i #체크된 인덱스값 넣어주기
            max_idx=num-1+i #체크된 인덱스값 넣어주기
        else:
            break #좌우대칭이 안됐을때

    for i in range(min_idx,max_idx+1):
            switch_lst[i]=(switch_lst[i]+1)%2 #체크된 인덱스의 스위치 바꿔주기


n=int(input())
switch_lst=list(map(int,input().split())) #스위치를 담은 리스트
stu=int(input()) # 학생수
stu_lst=[] # 학생 리스트
for _ in range(stu):
    sex,num=map(int,input().split())
    stu_lst.append((sex,num))



for x,y in stu_lst:
    if x==1:
        switch_status_m(y) # 성별 남자일때
    else:
        switch_status_w(y) # 성별 여자일때


for i in range(1,n+1):
    if i%20==0:
        print(switch_lst[i-1])
    else:
        print(switch_lst[i-1],end=" ")