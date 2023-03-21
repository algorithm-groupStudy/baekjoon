import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.ArrayDeque;

public class Main {
    static int n,m;
    static int alpha, beta;
    static boolean[] visited;
    static ArrayList<Integer>[] map;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException{
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());//사람 수
        visited = new boolean[n+1];
        //사람 인접리스트
        map = new ArrayList[n+1];
        for(int i=1;i<=n;i++) {
            map[i] = new ArrayList<>();
        }
        st = new StringTokenizer(br.readLine());
        alpha = Integer.parseInt(st.nextToken());
        beta = Integer.parseInt(st.nextToken());

        //부모자식
        m = Integer.parseInt(br.readLine());
        for(int i=0;i<m;i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            map[s].add(e);
            map[e].add(s);
        }
        System.out.println(bfs(alpha,beta));

    }
    static int bfs(int s, int e) {
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(s);
        visited[s] = true;

        int turn = -1;
        while(!q.isEmpty()) {
            turn++;
            int size = q.size();
            while(size-->0) {
                int cur = q.poll();
                if(cur==e) return turn;
                for(int n:map[cur]) {
                    if(visited[n]) continue;

                    visited[n] = true;
                    q.offer(n);
                }
            }
        }
        return -1;

    }
}