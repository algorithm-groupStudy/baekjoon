````java
#### [문제 정보]

>  implementation bj S5 time O 1505 CPU

#### [문제 요약]

> 문제 요약 및 추상화

#### [풀이 과정]

```java
	StringTokenizer st = new StringTokenizer(br.readLine());
	String opcode = st.nextToken();
	String rD = st.nextToken();
	String rA = st.nextToken();
	String rB = st.nextToken();
```

1. useC = 0;
2. opcode[-1]==C? ->useC=1, opcode = opcode[opcode.length-2,opcode.length-1]
3. res = opcode + useC + 0
4. res += 3단2진(rd)
5. res+=3단2진(ra)
6. useC? -> res+=4단2진(rb)
7. else? -> res+=3단2진(rb)+0

#### [시간 복잡도]

#### [틀린 이유]

#### [느낀점]

#### [해결 코드]



```java
package bj_CPU;
import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static HashMap<String,String> map = new HashMap<>();
	
	public static void main(String[] args) throws Exception{
		map.put("ADD","0000");
		map.put("SUB","0001");
		map.put("MOV","0010");
		map.put("AND","0011");
		map.put("OR","0100");
		map.put("NOT","0101");
		map.put("MULT","0110");
		map.put("LSFTL","0111");
		map.put("LSFTR","1000");
		map.put("ASFTR","1001");
		map.put("RL","1010");
		map.put("RR","1011");
		
		
		
		int t = Integer.parseInt(br.readLine());
		for(int tc = 0; tc<t;tc++) {
			bw.write(compile());
		}
		bw.close();
		
	}
	
	
	static String compile() throws Exception{
		StringBuilder res = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		String opcode = st.nextToken();
		String rD = st.nextToken();
		String rA = st.nextToken();
		String rB = st.nextToken();
		
		int useC = 0;
		if(opcode.substring(opcode.length()-1,opcode.length()).equals("C")) {
			useC = 1;
			opcode = opcode.substring(0,opcode.length()-1);
		}
//		System.out.println(opcode);
		res.append(map.get(opcode))
		.append(Integer.toString(useC)+"0")
		.append(toBin(Integer.parseInt(rD),3))
		.append(toBin(Integer.parseInt(rA),3));
		
		if(useC==1) {
			res.append(toBin(Integer.parseInt(rB),4));
		}else {
			res.append(toBin(Integer.parseInt(rB),3)+"0");
		}
		res.append("\n");
		
		
		
		
		
		
		
		
		return res.toString();
	}
	
	static String toBin(int num, int fill) {
		String res = "";
		while(num>0) {
			int mok = num/2;
			int mod = num%2;
			res = Integer.toString(mod)+res;
			num = mok;
		}
		while(res.length()<fill) {
			res = "0"+res;
		}
		return res;
	}

}

```xxxxxxxxxx package bj_CPU;import java.io.*;import java.util.HashMap;import java.util.StringTokenizer;public class Main {    static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));    static HashMap<String,String> map = new HashMap<>();        public static void main(String[] args) throws Exception{        map.put("ADD","0000");        map.put("SUB","0001");        map.put("MOV","0010");        map.put("AND","0011");        map.put("OR","0100");        map.put("NOT","0101");        map.put("MULT","0110");        map.put("LSFTL","0111");        map.put("LSFTR","1000");        map.put("ASFTR","1001");        map.put("RL","1010");        map.put("RR","1011");                                int t = Integer.parseInt(br.readLine());        for(int tc = 0; tc<t;tc++) {            bw.write(compile());        }        bw.close();            }            static String compile() throws Exception{        StringBuilder res = new StringBuilder();        StringTokenizer st = new StringTokenizer(br.readLine());        String opcode = st.nextToken();        String rD = st.nextToken();        String rA = st.nextToken();        String rB = st.nextToken();                int useC = 0;        if(opcode.substring(opcode.length()-1,opcode.length()).equals("C")) {            useC = 1;            opcode = opcode.substring(0,opcode.length()-1);        }//      System.out.println(opcode);        res.append(map.get(opcode))        .append(Integer.toString(useC)+"0")        .append(toBin(Integer.parseInt(rD),3))        .append(toBin(Integer.parseInt(rA),3));                if(useC==1) {            res.append(toBin(Integer.parseInt(rB),4));        }else {            res.append(toBin(Integer.parseInt(rB),3)+"0");        }        res.append("\n");                                                                        return res.toString();    }        static String toBin(int num, int fill) {        String res = "";        while(num>0) {            int mok = num/2;            int mod = num%2;            res = Integer.toString(mod)+res;            num = mok;        }        while(res.length()<fill) {            res = "0"+res;        }        return res;    }}java
````