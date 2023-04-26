/*
주헌고통지수는 최소값과 최대값만으로 계산하므로 정렬해서 스코빌 지수를 사용했다
연속된 k개의 음식을 조합으로 선택하게 되면 스코빌 지수가 가장 작은 음식과 가장 큰 음식을 제외한 k-2개의 음식은 선택되나 안되나 같으므로 2^(k-2)개의 경우가 있다.
연속된 k개의 음식은 0에서 k번째 음식, 1에서 k+1번째 음식, 2에서 k+2번째 음식, ... , n-1-k에서 n-1번째 음식이 있으니까 모든 경우를 더하면 가장 큰 음식 k-1개의 합 - 가장 작은 음식 k-1개의 합이다.
그래서 스코빌 지수의 합의 차이의 합에 2의 거듭제곱을 구해서 풀었다.
*/
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        long p = 1_000_000_007;
        int n = Integer.parseInt(br.readLine());
        long[] scores = new long[n]; // 각 음식의 스코빌 지수 저장
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            scores[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(scores); // 스코빌 지수 기준 정렬
        long answer = 0L; //주헌고통지수의 합
        long cur = 0L; // 스코빌 지수의 차의 합
        long power2n = 1L; // 2의 거듭제곱
        for (int i = 0; i < n; i++) {
            cur += scores[n-1-i] - scores[i] + p; // i번째 큰 스코빌 지수와 i번째 작은 스코빌 지수의 차이 더하기
            cur = (cur % p + p) % p; // 나누기
            answer += cur * power2n; // 2^i개의 경우가 있다
            answer %= p;
            power2n *= 2;
            power2n %= p;
        }
        bw.write(answer + "\n");
        bw.close();
        br.close();
    }
}