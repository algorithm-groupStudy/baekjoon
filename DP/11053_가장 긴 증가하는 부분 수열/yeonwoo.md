#### [문제 정보]

> {알고리즘} / {난이도} / {걸린시간} / {성공여부} / {제목(링크)}
>
> dp / bj_S2 / 120 / X / 가장 긴 증가하는 부분 수열(https://www.acmicpc.net/problem/11053)

#### [문제 요약]

> 제곧문

#### [풀이 과정]

1. `int[] arr`에 수열을  입력받는다

2. `arr`과  같은 크기의 배열 `int[] dp`를 만든다(용도: idx까지 오는 최대 거리 저장)

3. `dp[0] = 1`  첫 번째 요소까지 오는 가장 긴 거리는 무조건 1이다.

4. ans = 1 //최소 답 == 1 이므로

5. 2번째 요소부터 마지막 요소까지 for i loop 진행 (dp[i]를 구하기 위함)

   1. dp[i]  = 1 // 기본으로 i번 요소까지 오는 최대 거리는 1임

   2. 1번째 요소부터 i-1번쨰 요소까지  for j loop
      1. arr[i]보다 arr[j]가 작고, dp[i] <= dp[j]라면, dp[i] = dp[j]+1
   3. ans = max(ans, dp[i])

6. ans 출력

#### [시간 복잡도]

O(n^2)

#### [틀린 이유]

- 첫 알고리즘 고집함
- dp = 재귀라는 사고에 갇힘
- 30분넘기고도 계속 푼 이유: 풀지는 못했지만 dp 기본 문제라는 것을 알 수는 있었다. 기본 문제를 못 푸는 게 인정하기 어려웠다. 

#### [느낀점]

- 30/60/2 룰 지키기

#### [해결 코드 - java]
```java
package daily.y_2023.m_01.d_20.bj_11053_가장_긴_증가하는_부분_수열;
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        //String[] input = split(" ")과 속도 비교
        StringTokenizer st = new StringTokenizer(br.readLine());
        int arr[] = new int[n+1]; //수열 배열
        int dp[] = new int[n +1];//여기까지 오는 최대 길이

        for(int i=1;i<=n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dp[1] =1; //1까지 오는 최대길이 무조건 1
        int ans = 1; //최소 정답 1
        for(int i=2; i<=n;i++){ // 나
            dp[i] =1; //나는 1
            //나까지 오는 최대길이 구하기
            for(int j=1;j<i;j++){//이전것부터 나까지
                //내가 이전것보다 크고, 이전것까지 오는 최대길이가 나까지 오는 최대길이보다 크거나 같다
                if(arr[i] > arr[j] && dp[i] <= dp[j]){
                    dp[i] =dp[j]+1;//나까지 오는 최대길이 = {이전 것까지 오는 최대길이 +1}
                }
            }
            ans = Math.max(dp[i],ans);//max(나까지오는 최대길이(확정) vs ans)
        }

        bw.write(Integer.toString(ans));
        bw.flush();
        bw.close();
    }

}

```

#### [해결 코드 - python]

```python
n = int(input())

li = list(map(int,input().split()))
dp = [0 for col in range(n)] # col번째요소에 도달할 수 있는 최장거리 넣을 것

dp[0] = 1 #0번 요소까지 최장거리 무조건 1
res = 1 # 최소답 1

for i in range(1,n):
	dp[i] = 1 #최소 (최장거리)
	for j in range(0,i):
		if li[i]>li[j] and dp[i] <= dp[j]:
			dp[i] = dp[j]+1
	res = max(res,dp[i])

print(res)

```

