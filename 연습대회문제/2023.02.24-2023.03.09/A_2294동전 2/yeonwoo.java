import java.util.*;
import java.io.*;
/*
구상=2:25~2:30 (5)
구현=2:30~4:10 (100)

걍 짜면서 생각

//메모리초과 -< 해쉬셋 변경
 */
public class Main {
    static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    static int n,k;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        TreeSet<Integer> set = new TreeSet<>();

        for(int i=0;i<n;i++){
            set.add(Integer.parseInt(br.readLine()));
        }
        ArrayList<Integer> coins = new ArrayList<>(set);

        int[] dp = new int[k+1];
        for(int i=1;i<=k;i++){//dp 각 값 최대로 초기화
            dp[i] = Integer.MAX_VALUE;
        }


        for(int i=0;i<k;i++){
            // System.out.printf("k=%d\n",k);
            if(dp[i] == Integer.MAX_VALUE) continue;//못옴

            for(int j=0;j<coins.size();j++){
                int t =i+coins.get(j);
                if(t>k) break;

                dp[t] = Math.min(dp[i]+1,dp[t]);
                // System.out.printf("k=%d, dp[i]=%d, dp[t]=%d \n",k,dp[i],dp[t]);
            }
        }
        System.out.println(dp[k]==Integer.MAX_VALUE?-1:dp[k]);
    }






}