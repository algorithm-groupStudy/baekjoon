import java.io.*;
import java.util.PriorityQueue;
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException{
        PriorityQueue<Integer> pq = new PriorityQueue();

        int n = Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            int cur = Integer.parseInt(br.readLine());
            if(cur == 0 ){
                if(pq.isEmpty()){
                    bw.write("0\n");
                }else{
                    bw.write(Integer.toString(pq.poll())+"\n");
                }

            }
            else{
                pq.offer(cur);
            }
        }
        bw.flush();
        bw.close();

    }
}