import java.io.*;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    //peek을했는데 나보다 작아 -> pop하고 걔자리 내 수로

    static int n;
    static int[] arr;
    static int[] result;
    static StringTokenizer st;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException{
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }


        result = new int[n];
        Arrays.fill(result,-1);

        Stack<Integer> stack = new Stack<>();
        stack.push(0);

        for(int i=1;i<n;i++){
            while(!stack.isEmpty() && arr[stack.peek()]<arr[i]){
                int temp = stack.pop();
                result[temp] =arr[i];
            }
            stack.push(i);
        }

        for(int i=0;i<n;i++){
            bw.write(result[i]+" ");
        }
        bw.flush();
        bw.close();


    }
}
