import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;
public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N,K;
	static int[] prefer;
	//분산 평균 표준편차
	static double variance =0, tmp = 0, average = 0, stdDeviation=0;
	static double result = Double.MAX_VALUE;
	public static void main(String[] args) throws IOException{
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		//선호배열
		prefer = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {
			prefer[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i=0;i<=N-K;i++) {
			int count = K;//K개 이상이므로 K개부터 하나씩 늘려가면서 표편이 최소일 떄를 찾는다
			//배열의 끝까지 연속할 경우를 확인해야하므로 i+count가 N보다 작거나 같을때 까지만 반복
			while(i+ count <= N) {//이거 범위 안벗어남
				tmp = average = variance = stdDeviation = 0;
				for(int j=0;j<count;j++) {//i버째부터 count개 tmp에 더함
					tmp += prefer[i+j];
				}
				average = tmp/count;//평균
				tmp = 0;
				for(int j=0;j<count;j++) {//분산구하기
					tmp += (prefer[i+j]-average)*(prefer[i+j]-average);
				}
				variance = tmp/count;
				stdDeviation = Math.sqrt(variance); // 표준 편차 구하는 함수
				result = Math.min(result, stdDeviation); 
                count++;
				
			}
		}
		System.out.println(String.format("%.12f", result));
	}
}