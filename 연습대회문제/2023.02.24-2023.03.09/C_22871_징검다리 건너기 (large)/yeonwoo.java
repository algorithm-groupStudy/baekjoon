import java.io.*;
import java.util.*;

public class Main {
    static int n,k;
    static long[] arr, dp;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        arr =new long[n];
        dp = new long[n];
        st = new StringTokenizer(br.readLine());

        for(int i=0;i<n;i++){
            arr[i] = Long.parseLong(st.nextToken());
            dp[i] = -1;
        }

        System.out.println(jump(0));
    }

    static long jump(int x){
        if(x==n-1) return 0;
        if(dp[x] != -1){//이미처리한 장소
            return dp[x];
        }
        dp[x] = Long.MAX_VALUE;//내자리는 무한화
        for(int i=x+1;i<n;i++){//내자리부터 끝까지가면서
            //내자리부터 I자리까지 거리
            long xToi = (i-x)*(1+Math.abs(arr[x]-arr[i]));
            //i에서 끝까지 가는 거리 중 최대 단일 점프값
            long next = jump(i);
            long myK = Math.max(next, xToi);//xToi와 next중 큰 값이 x에서 i를 밟고 끝까지 갈 때 단일 이동 최댓값임

            //x에서 i를밟고 끝까지 갔을 때 최대 단일 이동 거리 VS x에서 ?를 밟고 끝까지 갔을 때 단일 최대거리
            dp[x] = Math.min(dp[x],myK); //둘 중 작은 값이 단일 최대 이동값의 최솟값임
        }
        return dp[x];
    }
}