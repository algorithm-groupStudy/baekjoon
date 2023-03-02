package daily.y_2023.m_03.d_02.bj_14722;

import java.io.*;
import java.util.StringTokenizer;

/*
60m
dp/bj  /G4  / 60 /X/14722/우유도시/https://www.acmicpc.net/problem/14722
 */
public class bj_14722_우유도시 {
    static int n;				// n x n 행렬
    static int[][] map;
    static int[][][] dp;
    static int maxCount;		// 출력, 마시는 우유 최대 개수


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in)
        );
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        map = new int[n + 1][n + 1];		// [1][1] ~ [n][n] 사용
        dp = new int[n + 1][n + 1][3];		// [0]행, [0]열은 패딩
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 1; j <= n; j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }

        //dp 부분 잘 보면 열별로 구하되 마지막 열에 가서는 앞전 행에서 구한 값도 반영됨을 알 수 있다
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                int currentMilk = map[i][j];	// 현재 위치의 우유

                // 우유 마시는 순서: 딸기(0) -> 초코(1) -> 바나나(2)
                if (currentMilk == 0) {
                    // 이전 순서의 바나나(2)를 최근으로 마신 개수 + 1
                    dp[i][j][0] = Math.max(dp[i][j-1][2] + 1, dp[i-1][j][2] + 1);
                }
                else {
                    dp[i][j][0] = Math.max(dp[i][j-1][0], dp[i-1][j][0]);
                }

                // 추가 조건식: 우유 마시는 순서 지키기 위함 (해당 현재 우유 currentMilk 를 마셔도 되는지 확인)
                if (currentMilk == 1 &&
                        dp[i][j][0] > dp[i][j][1]) {	// 이전에 딸기(0)를 먹었는지
                    // 이전 순서의 딸기(0)를 최근으로 마신 개수 + 1
                    dp[i][j][1] = Math.max(dp[i][j-1][0] + 1, dp[i-1][j][0] + 1);
                }
                else {
                    dp[i][j][1] = Math.max(dp[i][j-1][1], dp[i-1][j][1]);
                }

                if (currentMilk == 2 &&
                        dp[i][j][1] > dp[i][j][2]) {	// 이전에 초코(1)를 먹었는지
                    // 이전 순서의 초코(1)를 최근으로 마신 개수 + 1
                    dp[i][j][2] = Math.max(dp[i][j-1][1] + 1, dp[i-1][j][1] + 1);
                }
                else {
                    dp[i][j][2] = Math.max(dp[i][j-1][2], dp[i-1][j][2]);
                }
            }
        }

        // maxCount 찾기
        maxCount = Math.max(
                dp[n][n][0],
                Math.max(dp[n][n][1], dp[n][n][2])
        );
        System.out.println(maxCount);
    }
}