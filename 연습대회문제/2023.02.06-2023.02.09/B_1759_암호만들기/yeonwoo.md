#### [문제 정보]
>  Backtracking/ Bj_G5 / 30 / O / 암호만들기(https://www.acmicpc.net/problem/1759)

#### [문제 요약]

> 서로 다른 L개의 알파벳 소문자
>
> 최소 1개의 모음
>
> 최소 2개의 자음
>
> 알파벳 오름차순
>
> C개의 문자에서 암호가 가능한 모든 경우의 수를 구하라

#### [풀이 과정]

dfs depth == l이면 탈출 ()

c개의 암호 배열에 받아서정렬

배열0~끝까지순회

 c-idx+depth<L => return

#### [시간 복잡도]

O(2^N)

#### [틀린 이유]

#### [느낀점]

- 문제 조건 잘 챙기기(모음, 자음 조건 까먹었었음)
- 남은모음, 남은자음 개수 세서 가지치기 추가할 수 있을듯

#### [해결 코드]
```java
package bj.bj_1759;
import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] arsg) throws IOException{
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		
		int L = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		String[] words = new String[C];
		
		st= new StringTokenizer(br.readLine());
		for(int i=0;i<C;i++) {
			words[i] = st.nextToken();
		}
		Arrays.sort(words);

		//return;
		dfs("",0,0,L,C,words,bw,0,0);
		bw.flush();
		bw.close();
	}
	
	static void dfs(String res,int cIdx, int depth, int L, int C, String[] words, BufferedWriter bw,int moCnt, int jaCnt) throws IOException {
		if(depth==L) {
			if(moCnt<1||jaCnt<2) return;
			bw.write(res+"\n");
			return;
		}
		if(C-cIdx+depth<L) return;
		
		//사용
		if(words[cIdx].equals("a")||words[cIdx].equals("e")||words[cIdx].equals("i")||words[cIdx].equals("o")||words[cIdx].equals("u")) {
			dfs(res+words[cIdx],cIdx+1,depth+1,L,C,words,bw,moCnt+1,jaCnt);
		}else {
			dfs(res+words[cIdx],cIdx+1,depth+1,L,C,words,bw,moCnt,jaCnt+1);
		}
		//미사용
		dfs(res,cIdx+1,depth,L,C,words,bw,moCnt,jaCnt);
	}

}

```