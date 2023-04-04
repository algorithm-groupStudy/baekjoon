import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
/*
랜선 등록하면서 최댓값 선정
이진탐색
 각 선을 나눈 몫의 합이 N을 넘는 최댓값 탐색
*/
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int k, n;
    static long[] map;
    static long max = Long.MIN_VALUE;
    static long res = Integer.MIN_VALUE;
    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        map = new long[k];
        for(int i=0;i<k;i++){
            map[i] = Integer.parseInt(br.readLine());
            max = Math.max(max,map[i]);
        }
        Arrays.sort(map);
        max = map[map.length-1];

        binarySearch(1,max);
        System.out.println(res);
    }

    static void binarySearch(long s, long e){
        // System.out.println("s = " + s);
        // System.out.println("e = " + e);
        if(s>=e){
            if(check(e)){
                res = Math.max(res,e);
            }
            return;
        }
        long mid = (s+e)/2;
        // System.out.println("mid = " + mid);
        if(check(mid)){
            // System.out.println("res = " + res);
            res = Math.max(res,mid);
            // System.out.println("res = " + res);
            binarySearch(mid+1,e);
        }else{
            binarySearch(s,mid);
        }


    }
    static boolean check(long val){
        long sum = 0;
        for(int i=map.length-1;i>=0;i--){
            sum += map[i]/val;
            if(sum>=n) return true;
        }
        return false;
    }
}
