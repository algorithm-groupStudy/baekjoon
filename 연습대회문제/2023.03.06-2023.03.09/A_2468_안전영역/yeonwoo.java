import java.io.*;
import java.util.Queue;
import java.util.ArrayDeque;
import java.util.StringTokenizer;
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,-1,0,1};

    static int N;
    static int[][] map;
    static int high;
    static boolean[][] visited;

    static int finalRes = 0;
    public static void main(String[] args) throws IOException{
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];

        for(int i=0;i<N;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                high = Math.max(high, map[i][j]);
            }
        }

        //high설정
        while(high>0) {
            high--;
            visited = new boolean[N][N];
            int curRes = 0;
            for(int i=0;i<N;i++) {
                for(int j=0;j<N;j++) {
                    if(visited[i][j]) continue;
                    if(map[i][j]<=high) continue;
                    curRes ++;
                    bfs(i,j);
                }
            }
            finalRes = Math.max(finalRes, curRes);
        }
        System.out.println(finalRes);



    }

    static void bfs(int sr, int sc) {
        Queue<int[]> q= new ArrayDeque<>();
        q.offer(new int[] {sr,sc});
        visited[sr][sc] = true;

        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0];
            int c = cur[1];

            for(int i=0;i<4;i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if(nr<0||nr>=N||nc<0||nc>=N) continue;//범위초과
                if(visited[nr][nc]) continue;
                if(map[nr][nc]<=high) continue;

                visited[nr][nc] = true;
                q.offer(new int[] {nr,nc});
            }
        }
    }
}