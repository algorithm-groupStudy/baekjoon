```java
import java.io.*;
import java.util.TreeSet;
public class Main{
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int N;
	static int[][] dots;
	static int result = Integer.MAX_VALUE;
	public static void main(String[] args) throws IOException{
		N = Integer.parseInt(br.readLine());
		dots = new int[N][2];//점 담아둘 배열
		
		TreeSet<Integer> treeX = new TreeSet<>();
		TreeSet<Integer> treeY = new TreeSet<>();
		
		//점 배열 구성
		for(int i=0;i<N;i++) {
			String[] xy = br.readLine().split(" ");
			int x= Integer.parseInt(xy[0]);
			int y = Integer.parseInt(xy[1]);
			
			dots[i][0] = x; //x
			treeX.add(x);
			
			dots[i][1] = y; //y
			treeY.add(y);
		}
		Integer[] arrx = treeX.toArray(new Integer[0]);
		Integer[] arry = treeY.toArray(new Integer[0]);		
		
		for(int x1=0;x1<arrx.length;x1++) {
			for(int x2=x1;x2<arrx.length;x2++) {
				int y1 = 0;//x축에 가까운 y점
                int y2 = 0;//x축에서 먼 y점
                while(y2 < arry.length && y1 < arry.length){
                    int cnt = getNcount(arrx[x1],arrx[x2],arry[y1],arry[y2]);//임의의 사각형
                    if(cnt >= N/2){
                    	result = Math.min(getArea(arrx[x1],arrx[x2],arry[y1],arry[y2]), result);
                        y1++;
                    } else{
                    	y2++;
                        
                    }
                }
			}
		}
		System.out.println(result);
	}
	
	static int getNcount(int x1, int x2, int y1, int y2) {
//		System.out.println(String.format("XY:%s, %s -- %s,%s",x1,y1,x2,y2));
		int result = 0;
		for(int[] p : dots) {
//			System.out.println(String.format("pp:%s & %s",p[0],p[1]));
			int px = p[0];
			int py = p[1];
			
			if(x1 <= px && x2 >= px && y1 <= py && y2 >= py) {
				result ++;
			}
		}
		return result;
	}
	
	static int getArea(int x1, int x2, int y1, int y2) {
		return (Math.abs(x2-x1)+2) * (Math.abs(y2-y1)+2);
	}
	
}
```

