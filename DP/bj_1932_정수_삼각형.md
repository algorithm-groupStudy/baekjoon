#### [문제 정보]
>  {알고리즘} / {난이도} / {걸린시간} / {성공여부} / {제목(링크)}
>
>  Dynamic Programming / bj_S1 / 30- / O / 정수 삼각형(https://www.acmicpc.net/problem/1932)

#### [문제 요약]

> 인간 피라미드에 인간 대신 정수가 들어있는 모양의 [정수 피라미드]가 있다.
>
> 꼭대기에서 출발하여 바닥까지 오는 경로 중, 거쳐온 경로에 있는 숫자의 합이 가장 큰 경우 숫자의 합은?
>
> (단, 한 층에서 하나의 숫자만 선택 가능하고, 인접한 노드로만 이동 가능하다)

#### [풀이 과정]

1. `int n `에 피라미드 크기 받음 

   - 피라미드 크기 == 맨 아랫층 크기 == 피라미드 높이

2. `int[n][n] map`을 만들어 별 피라미드를 표현한다.

   - 각 층을 나타내는 column은 column[0 : 층의 요소 수] 까지가 채워진다

   - `map[0][0]`에 꼭대기 값이 들어가고, 

   - `map[r][c]`와 인접한 윗층 요소는 `map[r-1][c-1]`(윗층 왼쪽), `map[r-1][c]`(윗측 오른쪽)이다.

2. `int[n][n] dp`를 만들어 현재 좌표까지 도달하는 가장 큰 값을 저장하는 용도로 사용
   - `dp[0][0] = map[0][0]`임
3. for( int i=1; i<n;i ++) //위에서 2번째 층부터 바닥 층까지 순회
   1. for(int j=0;j<i+1;j++)//0열부터 i열까지 순회
      1. `dp[i][j] `= 인접한 윗층 요소 중 더 큰 요소 + `map[i][j]`
         - 이때 인접한 윗층 요소가 하나인 경우 있을 수 있으니 그부분 조건 걸어야함
4. dp배열 맨 아래층 중 가장 큰 값이 정답임



#### [시간 복잡도]

**O(n^2)**

1. for loop의 양상이 1+2+3+...+4+5+n-1
2. n까지의 모든 자연수를 더하는 공식 n(n+1)/2

#### [틀린 이유]

#### [느낀점]
#### [해결 코드]
```java
package daily.y_2023.m_01.d_21;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException{
        int n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        int[][] dp = new int[n][n];

        for(int i=0;i<n;i++){
            String[] input = br.readLine().split(" ");
            for(int j=0;j<input.length;j++){
                map[i][j] = Integer.parseInt(input[j]);
            }
        }

        dp[0][0] = map[0][0];
        for(int i=1; i<n; i++){
            for(int j=0;j<i+1;j++){
                getMax(i,j,map,dp, n);
            }
        }
        int result = 0;
        for(int i=0;i<n;i++){
            result = Math.max(dp[n-1][i],result);
        }
        bw.write(Integer.toString(result));
        bw.flush();
        bw.close();

        // printMap(map);
    }
    static void getMax(int r, int c, int[][] map, int[][] dp, int maxRange){
        if(c==maxRange-1){
            dp[r][c] = dp[r-1][c-1]+map[r][c];
        }else if(c-1<0){
            dp[r][c] = dp[r-1][c] + map[r][c];
        }else{
            dp[r][c] = Math.max(dp[r-1][c],dp[r-1][c-1]) + map[r][c];
        }
    }

    static void printMap(int[][] map){
        System.out.println();
        for(int i=0;i<map.length;i++){
            for(int j=0;j<map[0].length;j++){
                System.out.printf("%d ",map[i][j]);

            }
            System.out.println();
        }
    }
}

```