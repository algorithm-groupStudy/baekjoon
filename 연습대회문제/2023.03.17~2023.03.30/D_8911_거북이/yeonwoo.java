//package daily.y_2023.m_03.d_27.bj_8911_거북이;
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    //상우하좌
    static int[] dr = {1,0,-1,0};
    static int[] dc = {0,1,0,-1};

    static char[] orderArr;

    static int dir;

    static int curR,curC;
    static int maxR,maxC,minR,minC;

    static int res;

    public static void main(String[] args) throws IOException{
        int tc = Integer.parseInt(br.readLine());
        for(int t =0;t<tc;t++){
            int curRes= cal();
            bw.write(Integer.toString(curRes)+"\n");
        }
        bw.close();
    }

    static int cal() throws IOException{
        orderArr = br.readLine().toCharArray();
        dir = 0;//상방향 시작
        //시작위치
        curR = 0;
        curC = 0;
        maxR=minR=maxC=minC=0;
        for(char c:orderArr){
            if(c=='R'){
                rTurn();
            }else if(c=='L'){
                lTurn();
            }else if(c=='F'){
                go();
                check();
            }else if(c=='B'){
                goBack();
                check();
            }
            else{
                throw new RuntimeException("불가한 경우");
            }
        }
        // System.out.printf("maxR=%d minR=%d maxC=%d minC=%d\n",maxR,minR,maxC,minC);
        return (maxR-minR)*(maxC-minC);
    }
    static void rTurn(){
        dir=(dir+1)%4;
    }
    static void lTurn(){
        for(int i=0;i<3;i++){
            rTurn();
        }
    }
    static void goBack(){
        rTurn();
        rTurn();
        go();
        rTurn();
        rTurn();
    }
    static void go(){
        curR+=dr[dir];
        curC+=dc[dir];
    }
    static void check(){
        maxR = Math.max(curR,maxR);
        minR = Math.min(curR,minR);

        maxC = Math.max(curC,maxC);
        minC = Math.min(curC,minC);
    }
}
