import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException{
        PriorityQueue<Long> pq = new PriorityQueue(new Comparator<Long>(){

            public int compare(Long a, Long b){
                if(Math.abs(a)<Math.abs(b)){
                    return -1;
                }else if(Math.abs(a)>Math.abs(b)){
                    return 1;
                }
                return a.compareTo(b);

            }
        });

        int n = Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            long cur = Long.parseLong(br.readLine());
            if(cur == 0 ){
                if(pq.isEmpty()){
                    bw.write("0\n");
                }else{
                    bw.write(Long.toString(pq.poll())+"\n");
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