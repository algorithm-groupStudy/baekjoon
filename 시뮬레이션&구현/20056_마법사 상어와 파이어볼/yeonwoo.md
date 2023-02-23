

## #구상

### 시작시간: 15:25 , 종료시간:15:55 (구상 소요 시간:30 )



#### [문제 정보]

>  algo / platform / rate / time / isSuccess / no / title / link
>
>  implementation /bj / G3/ 120 ++ / X / 20056 /마법사 상어와 파이어 볼

#### [문제 요약] 

> n+1*n+1배열에서 논다(배열번호 1부터)
>
> M개파볼
>
> K번이동
>
> 파이어볼(r, c, m, d, s)
>
> 파이어볼방향 d = 상우하좌 8방
>
> #### 아래는 k번 반복
>
> 1. d방향으로 s칸 이동(이동중 충돌 무시)
> 2. 같은 칸에 2개 이상 겹치면 파이어볼 4개로 분쇄
>    1. 각 파이어볼 무게  = sum(동일칸파이어볼질량)/5
>       1. 만약 질량 0이면 소멸
>    2. 각 파이어볼 속력 = sum(동이랔파이어볼속력)/num(동일칸파이어볼)
>    3. 각 파이어볼 방향
>       1. 합처진 파이어볼 방향이 모두짝수 or 모두 홀수 -> 0,2,4,6
>       2. else -> 1,3,5,7

#### [풀이 과정]

```markdown
0. FireBall class
생성자 r,c,m,s,d

1. static 영역
int[] dr, dc
int N,M,K
`Queue<FireBall>[][] map;`
`ArrayList<FireBall> fireBalls;`

2. main영역
N,M,K 초기호
map N,N 설정 후 큐 만들어주기

2-1 M번반복
FireBall 객체 생성
	fBalls.add 해당객체

K번반복
K-1. 이동
for(FireBall fb:fireBalls):
	fb.r = (fb.r + dr[fb.d] * fb.s) %N
	fb.c = (fb.c + dc[fb.d] * fb.s) %N
	map[fb.r][fb.c].offer(fb)

K-2. 결합 및 분배
for i in range(N):
	for j in range(N):
		if(map[i][j].size<2):
			map[i][j].clear
			continue;
		//현재좌표 파볼 큐
		Queue<FireBall> curQ = map[i][j];
		
		//새로만들어질 파볼
		int sumM = 0;
		int sumS = 0;
		int num = q.size()
		int odd = 0;
		int even = 0;
		
		while(size-->0){
			FireBall fb = q.poll();
			sumM += fb.m;
			sumS += fb.s;
			num++;
			if(fb.d%2==0) even++;
			else odd++;
			//리스트에서 제거
			fireBalls.remove(fb);
		}
		if(sumM/5==0) continue; //질량0으로 나눠짐
		if(odd==0 || even==0){
			list.add(new FireBall(i,j,sumM/5,sumS/num,0));
            list.add(new FireBall(i,j,sumM/5,sumS/num,2));
            list.add(new FireBall(i,j,sumM/5,sumS/num,4));
            list.add(new FireBall(i,j,sumM/5,sumS/num,6));
		}else{
			list.add(new FireBall(i,j,sumM/5,sumS/num,1));
            list.add(new FireBall(i,j,sumM/5,sumS/num,3));
            list.add(new FireBall(i,j,sumM/5,sumS/num,5));
            list.add(new FireBall(i,j,sumM/5,sumS/num,7));		
		}
		
		
		
		
		
	


```





#### [시간 복잡도]

모름

#### [테스트케이스]

```markdown
//8
4 2 1
1 1 5 2 2
1 4 7 1 6
//9
7 5 3
1 3 5 2 4
2 3 5 2 6
5 2 9 1 7
6 2 1 3 5
4 4 2 4 2
```



## #구현

### 시작시간:16:00 , 종료시간: (구현 소요 시간: )



#### [해결 코드] 

```java
public class Main{
    public static void main(String[] args){
        //code
    }
}
```





#### [틀린 이유]

#### [느낀점]

1. 정말 이정도는 구현에서 해도 된다고 생각한 경우가 있고
2. 1이라고 합리화하지만 사실은 지금 생각하기 부담되는 경우가 있다.

1이어도 구현단계에서 설계를 보고 구현하다보면 헷갈리는데 2면 정말 난처해진다.

조바심이 느껴져도 설계단계에서 철저히 해두어야 구현에서 문제가 안 생기는 것 같다.