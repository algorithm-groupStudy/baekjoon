//package dfs_bfs.d_2022_09_30.bj_7569;
import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;

    static int N, M, H;

    static int[] dr = {0,0,-1,0,1,0};
    static int[] dc = {0,0,0,-1,0,1};
    static int[] dh = {-1,1,0,0,0,0};


    public static void main(String[] args) throws IOException{
        st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());//rows
        N = Integer.parseInt(st.nextToken());//cols
        H = Integer.parseInt(st.nextToken());//highs

        int[][][] map = new int[H][N][M];
        int count = 0; // 익혀야할 도마도의 수
        ArrayList<int[]> list = new ArrayList<>();//익은 도마도

        for(int h=0;h<H;h++) {
            for (int n = 0; n < N; n++) {
                st = new StringTokenizer(br.readLine());
                for (int m = 0; m < M; m++) {
                    int cur = Integer.parseInt(st.nextToken());
                    map[h][n][m] = cur;

                    if(cur==0) count++;
                    else if(cur==1){
                        list.add(new int[] {h,n,m});
                    }
                }
            }
        }

        boolean[][][] visited = new boolean [H][N][M];
        int result = bfs(map,count,visited,list);
        bw.write(Integer.toString(result)+"\n");
        bw.flush();
        bw.close();
    }
    static int bfs(int[][][] map,int count,boolean[][][] visited,ArrayList<int[]> list){
        int result = -1;
        //[h,n,m]
        Queue<int[]> q= new LinkedList<>();

        for(int[] node:list){
            q.offer(node);
            int h = node[0];
            int n= node[1];
            int m = node[2];
            visited[h][n][m] = true;
        }

        while(!q.isEmpty()){
            int size = q.size();
            result ++;
            while(size-->0) {
                int[] cur = q.poll();
                int ch = cur[0];
                int cr = cur[1];
                int cc = cur[2];

                for (int i = 0; i < 6; i++) {
                    int nh = ch + dh[i];
                    int nr = cr + dr[i];
                    int nc = cc + dc[i];

                    if (nh < 0 || nh >= H) continue;
                    if (nr < 0 || nr >= N) continue;
                    if (nc < 0 || nc >= M) continue;
                    if (visited[nh][nr][nc]) continue;
                    if(map[nh][nr][nc]!=0) continue;
                    visited[nh][nr][nc] = true;
                    q.offer(new int[]{nh, nr, nc});
                    count--;
                }
            }
        }
        if(count==0) return result;
        else return -1;
    }
}
