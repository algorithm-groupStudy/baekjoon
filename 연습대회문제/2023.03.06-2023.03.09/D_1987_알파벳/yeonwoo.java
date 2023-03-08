import java.io.*;
import java.util.Queue;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,-1,0,1};

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static char[][] map;
    static boolean[][] visited;
    static boolean[] use = new boolean[91];//알파벳
    static int R,C;

    static int max = Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException{

        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];
        visited = new boolean[R][C];

        for(int i=0;i<R;i++) {
            map[i] = br.readLine().toCharArray();
        }
        use[(int)map[0][0]] = true;
        dfs(0,0,1);
        System.out.println(max);

    }

    static void dfs(int sr,int sc, int depth) {
        max = Math.max(max, depth);
        for(int i=0;i<4;i++) {
            int nr = sr+dr[i];
            int nc = sc+dc[i];

            if(!isIn(nr,nc)) continue;
            if(visited[nr][nc]) continue;

            char cur = map[nr][nc];
            if(isUse(cur)) continue;

            visited[nr][nc] = true;
            use[(int)cur] = true;
            dfs(nr,nc,depth+1);
            visited[nr][nc] = false;
            use[(int)cur] = false;



        }
    }
    static boolean isUse(char c) {
        if(use[(int)c]) return true;
        return false;
    }

    static boolean isIn(int r, int c) {
        return r>=0 && r<R && c>=0 && c<C;
    }
}