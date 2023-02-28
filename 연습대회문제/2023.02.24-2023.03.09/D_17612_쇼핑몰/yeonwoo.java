package daily.y_2023.m_02.d_28.bj_17612_쇼핑몰;
import java.io.*;
import java.math.BigInteger;
import java.util.*;

//시작=2:55, 종료=4:15, 총소요시간=80분
//어려웠던 점 = long에 담기지 않는 범위라고는 생각하지 못했다.
/*
카트 수, 계산대 수
카트배열 초기화
계산대 배열 초기화

카트배열 값 채우고
계산대 pq 만들어서 계산대 다 넣기


1. 카트배정
PriorityQueue<계산대>
1. 짧은대기시간
2. 앞번호

2. 손님탈출
뒷계산대부터 1분씩 줄인다
줄이니까 0되면 아이디 기록하고
count ++
count == N? --> 계산

 */

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N;//카트 수
    static Cart[] cartArr;//카트 배열
    static int outN=0;//나간카트수

    static int k;//계산대 수
    static Cashier[] cashierArr;

    static class Cart{
        int id;
        int w;
        public Cart(int id, int w){
            this.id = id;
            this.w = w;
        }
    }
    static class Cashier implements Comparable<Cashier>{
        int no;
        Queue<Cart> q;
        int time;
        public Cashier(int no){
            this.no = no;
            this.q = new ArrayDeque<>();
            this.time = 0;
        }
        void addCart(Cart c){
            this.q.offer(c);
            this.time+=c.w;
        }

        @Override
        public int compareTo(Cashier o){
            if(this.time==o.time){//시간 같으면 넘버 앞인애가 먼저
                return this.no-o.no;
            }

            return this.time-o.time;//기본적으로 시간순
        }


    }
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        cartArr = new Cart[N];//카트배열 초기화
        cashierArr = new Cashier[k];//캐셔배열 초기화

        for(int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            int id = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            cartArr[i] = new Cart(id,w);
        }

        //캐셔pq
        PriorityQueue<Cashier> pq = new PriorityQueue<>();
        //캐셔 k개 생성 및 pq에 넣기
        for(int i=0;i<k;i++){
            cashierArr[i] = new Cashier(i);
            pq.offer(cashierArr[i]);
        }

        //순서대로 카트 배정
        for(int i=0;i<N;i++){
            Cart curCart = cartArr[i];//이번에 들어갈 카트
            Cashier minCashier = pq.poll();//최저 캐셔

            minCashier.addCart(curCart);
            // System.out.printf("%d번 캐셔에 id=%d,w=%d인 카트 배정\n",minCashier.no,curCart.id,curCart.w);
            pq.offer(minCashier);
        }

        ArrayList<Integer> outList = new ArrayList<>();
        //캐셔 역순 포문 돌면서 카트 뽑기
        while(outN<N) {
            for (int i = k - 1; i >= 0; i--) {
                Cashier curCashier = cashierArr[i];
                Queue<Cart> q = curCashier.q;//현재 캐셔의 카트큐
                if(q.isEmpty()) continue;

                Cart curCart = q.peek();//나와야되는 카트
                curCart.w -= 1;
                //다기다림
                if (curCart.w == 0) {
                    outList.add(curCart.id);
                    outN++;
                    q.poll();
                    continue;
                }
            }
        }
        // System.out.println(outList);
        BigInteger result = BigInteger.valueOf(0);
        // int[] temp = {123, 21, 56, 723, 45, 34, 55, 13,  910,73};
        // outList.clear();
        // for(int t:temp){
        //     outList.add(t);
        // }
        // outList =  Arrays.asList(temp);
        for(int i=0;i<outList.size();i++){
            int id = outList.get(i);
            BigInteger bigId = BigInteger.valueOf(id);
            BigInteger idxNum = BigInteger.valueOf(i+1);
            bigId = bigId.multiply(idxNum);

            result = result.add(bigId);
        }
        System.out.println(result.toString());


    }
}
/*
카트 수, 계산대 수
카트배열 초기화
계산대 배열 초기화

카트배열 값 채우고
계산대 pq 만들어서 계산대 다 넣기


1. 카트배정
PriorityQueue<계산대>
1. 짧은대기시간
2. 앞번호

2. 손님탈출
뒷계산대부터 1분씩 줄인다
줄이니까 0되면 아이디 기록하고
count ++
count == N? --> 계산

 */
