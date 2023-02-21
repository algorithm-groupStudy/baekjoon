

#### [문제 정보]

>  algo_platform_rate_time_isSuccess_no_title_link
>
>  implementation/bj/S2/7시간30분/X/16113/시그널

#### [문제 요약] 시작시간: 15:30

> 문제 요약 및 추상화
>
> .=0
>
> #=1
>
> 

#### [풀이 과정]

1. 행길이 5의 배수로 나눔 = mok

2. boolean[5] [mok] 배열 mpa생성

3. for(int i=0; i<mok;i++){

   1. 이번수 = -1

   ​	if (map[0] [i])이번수 =  0~9체커(0,i)

   }

4. 이번수가 1이면 i++, else i+=2



체커: 하나하나 넣음

#### [시간 복잡도]

최악에 모든 배열 요소 다 뒤지니까 O(N)아닌가?



#### [테스트케이스]

```
//8317
90
###.....###.#..####.#.......#.#....####.....###.#....##.#.......#.#....####.....###.#....#

//0
15
####.##.##.####

//8 1
40
###..#..#.#..#..###..#..#.#..#..###..#..


//1 1
15
#.##.##.##.##.#
```



#### [해결 코드] 시작시간:15:55(설계 소요시간: 25분)

```java
//package daily.y_2023.m_02.d_20.bj_시그널;

import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[] res = {1,7,4,2,3,5,6,9,0,8};
    static int[][] oneChecker = {
            {0,1},{1,1},{2,1},{3,1},{4,1}
    };
    static int[][][] checker = {
            {{0,-1},{1,-1},{2,-1},{3,-1},{4,-1},{0,1},{1,1},{2,1},{3,1},{4,1}},//1
            {{1,0},{2,0},{3,0},{4,0},{1,1},{2,1},{3,1},{4,1}},//7
            {{0,1},{1,1},{3,0},{3,1},{4,0},{4,1}},//4
            {{1,0},{1,1},{3,1},{3,2}},//2
            {{1,0},{1,1},{3,1},{3,0}},//3
            {{3,0},{3,1},{1,1},{1,2}},//5
            {{1,1},{1,2},{3,1}},//6
            {{1,1},{3,0},{3,1}},//9
            {{1,1},{2,1},{3,1}},//0
            {{1,1},{3,1}}//8
    };
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        String signal = br.readLine();

        int mok = n / 5;
        boolean[][] map = new boolean[5][mok];
        int stringIdx = 0;
        // map 초기화
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < mok; j++) {
                String cur = signal.substring(stringIdx, stringIdx + 1);

                boolean curIn = cur.equals("#") ? true : false;
                map[i][j] = curIn;
                stringIdx++;
            }
        }
//		printArr(map);

        for (int i = 0; i < mok; i++) {
            int cur = -1;
            if (map[0][i])
                cur = numChecker(0, i,map);// 뭔가존재함
            if (cur == -1) {// 숫자없음
                continue;
            } else {// 숫자있음
                bw.write(Integer.toString(cur));// 답에등록
                if (cur == 1)
                    i++;
                else
                    i += 3;
            }

        }
        bw.close();
    }
    static void printArr(boolean[][] map) {
        System.out.println();
        for(int i=0;i<map.length;i++) {
            for(int j=0;j<map[0].length;j++) {
                System.out.print(map[i][j]+ " ");
            }
            System.out.println();
        }
    }

    static int numChecker(int sr, int sc, boolean[][] map) {
        int nr, nc;
		// System.out.printf("시작행열 %d, %d\n",sr,sc);

        //TODO 앞뒤범위초과시 1
        // if(!isIn(map,sr,sc-1) && !isIn(map,sr,sc+1)) {
        if(!isIn(map,sr,sc+1)) {
			// System.out.println("code0");
            // System.out.printf("%d행 %d열 범위초과로 1\n",sr,sc+1);
            return 1;
        }
        boolean isOne = true;
        for(int i=0;i<5;i++){
            nr = sr + oneChecker[i][0];
            nc = sc + oneChecker[i][1];

            // System.out.printf("%d, %d = %s\n",nr,nc,map[nr][nc]);
            if(map[nr][nc]) {
                isOne = false;
                break;
            }
        }
        if(isOne) {
            // System.out.println(333);
            return 1;
        }

        //0~9 중에 뭔지 알아내는 로직
        for(int i=0;i<10;i++) {
            boolean flag = true;//숫자찾았나 확인용
			// System.out.println(res[i]+"ㄷ탐색 ###############");
            for(int[] rc : checker[i]) {//dr dc같은거, 빈칸체크용

                nr = sr+rc[0];
                nc = sc+rc[1];
				// System.out.printf("현재탐색행열 %d, %d = ", nr,nc);
                // if(nr==-1) {
                //     // System.out.println("1번 거르고");
                //     continue;//1은따로체크할꺼
                // }

                if(!isIn(map,nr,nc)) {
					// System.out.println("code1");
                    flag = false;
                    break;
                }
                if(map[nr][nc]) {
					// System.out.println("채워져있음");
                    flag = false;
                    break;//빈공간 불일치
                }
				// System.out.println("비어있음");
                // flag = true;//빈공간 모두 일치
            }
            if(flag) {
				// System.out.println(res[i]+"가 숫자");
                return res[i];
            }
        }
		// System.out.println("code2");
        return -1289;//다안맞으면 1임

    }

    static boolean isIn(boolean[][] map, int r, int c) {
        int maxR = map.length;
        int maxC = map[0].length;
        return r < maxR && r >= 0 && c < maxC && c >= 0;
    }
}


```

#### 종료시간: 20:50 (구현 소요시간 : 5시간)



#### [틀린 이유]

- 쫄았음
- 마지막테케 1예외 처리 못했음

#### [느낀점]

구현은 너무 어렵다
