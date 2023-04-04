import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n;

    static int[] arr;
    static Stack<Node> s = new Stack<Node>();


    public static void main(String[] args) throws IOException{
        n = Integer.parseInt(br.readLine());
        arr = new int[n];

        //
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++) {
            int val = Integer.parseInt(st.nextToken());//현재수

            int num =i;//현재수 인덱스
            Node n = new Node(i+1,val);
            while(true) {
                if(s.empty()) {//스택빔?
                    s.push(n);//나 들어가
                    arr[i] = 0;
                    break;//다음숫자달려
                }

                //스택안빔?
                Node peek = s.peek();//맨위수
                if(peek.val<n.val) {//나보다작아?
                    s.pop();//버려
                }else if(peek.val>=n.val) {
                    s.push(n);
                    arr[i]=peek.idx;
                    break;
                }
                num--;


            }

            bw.write(arr[i]+" ");
        }
        bw.close();


    }

    static class Node{
        int idx, val;
        public Node(int idx, int val) {
            this.idx = idx;
            this.val = val;
        }
    }

}
