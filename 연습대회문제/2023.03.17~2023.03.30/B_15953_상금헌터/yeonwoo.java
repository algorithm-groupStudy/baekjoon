package daily.y_2023.m_03.d_22;
import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int T;
    static StringTokenizer st;
    static int[] dp1 = new int[22];
    static int[] dp2 = new int[32];
    static int[] f1 = {0,500,300,200,50,30,10};
    static int[] f2 = {0,512,256,128,64,32};
    public static void main(String[] args) throws IOException{
        int idx=1;
        for(int grade=1;grade<=6;grade++){
            for(int i=0;i<grade;i++){
                dp1[idx++]=f1[grade];
            }
        }

        idx=1;
        for(int grade=1;grade<=5;grade++){
            for(int i=0;i<Math.pow(2,grade-1);i++){
                dp2[idx++]=f2[grade];
            }
        }

        // System.out.println(Arrays.toString(dp1));
        // System.out.println(Arrays.toString(dp2));
        T = Integer.parseInt(br.readLine());
        for(int i=0;i<T;i++){
            st = new StringTokenizer(br.readLine());
            int f = Integer.parseInt(st.nextToken());
            int ff = Integer.parseInt(st.nextToken());

            int p1 = f<dp1.length?dp1[f]:0;
            int p2 = ff<dp2.length?dp2[ff]:0;
            // System.out.printf("%d, %d\n",p1,p2);
            int res=p1+p2;
            if(i<T-1){
                bw.write(res>0?Integer.toString(p1+p2)+"0000\n":"0\n");
            }else{
                bw.write(res>0?Integer.toString(p1+p2)+"0000":"0");
            }

        }
        bw.close();

    }

}
