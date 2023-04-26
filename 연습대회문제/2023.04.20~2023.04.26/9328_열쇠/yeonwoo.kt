import java.io.*
import java.util.*

val br = BufferedReader(InputStreamReader(System.`in`))
val bw = BufferedWriter(OutputStreamWriter(System.out))

val dr = intArrayOf(-1,0,1,0)
val dc = intArrayOf(0,-1,0,1)

fun main(){
    val T = br.readLine().toInt()
    for(tc in 0 until T){
        cal()
    }
    bw.close()
}

fun cal(){
    //열쇠 초기화
    val key = Array<Boolean>(26){false}

    //알파벳별 문 위치
    val gates:Array<MutableList<Array<Int>>> = Array(26){ mutableListOf() }//열지 못한 문

    //높이, 너비
    val st = StringTokenizer(br.readLine())
    val h = st.nextToken().toInt()
    val w = st.nextToken().toInt()

    //맵 세팅
    val map = Array<Array<Char>>(h+2){Array<Char>(w+2){'.'} }

    //사무실 내부
    for(i in 1 .. h){
        val line = br.readLine().toCharArray()
        for(j in 1..w){
            map[i][j] = line[j-1]
        }
    }

    //보유중인 열쇠
    val haveKey = br.readLine()
    if(!haveKey.equals("0")){//0이면 key 없음
        for(c:Char in haveKey){
            key[c-'a'] = true//있는 키 보유처리
        }
    }

    //bfs
    val res = bfs(map,key, gates)
    bw.write(res.toString()+"\n")
}

fun bfs(map: Array<Array<Char>>,key:Array<Boolean>, gates:Array<MutableList<Array<Int>>>):Int{
    val wholeH = map.size //여백포함 높이;
    val wholeW = map[0].size //여백포함 너비

    //bfs 기본재료
    var res = 0
    val q = ArrayDeque<Array<Int>>()

    val visited = Array<Array<Boolean>>(wholeH){Array<Boolean>(wholeW){false} }
    //0,0에서 시작
    q.offer(Array<Int>(2){0})
    visited[0][0] = true

    while(!q.isEmpty()){
        val r = q.peek()[0]
        var c = q.poll()[1]

        //4방탐색
        for(i in 0 until 4){
            val nr = r+dr[i]
            val nc = c+dc[i]

            if(nr<0 || nr>=wholeH || nc<0 || nc>=wholeW) continue //범위초과
            if(visited[nr][nc]) continue //방문초과
            if(map[nr][nc] == '*') continue //벽초과

            val elem = map[nr][nc] //새 값
            if(elem in 'A'..'Z'){
                //문 발견!

                if(key[elem-'A']){
                    //열쇠 있따!!

                    map[nr][nc] = '.';//빈 공간화 -- 없애도 될듯?
                    visited[nr][nc] = true;

                    q.offer(arrayOf<Int>(nr,nc))
                }else{
                    //열쇠 없다!!

                    gates[elem-'A'].add(arrayOf<Int>(nr,nc))//이 알파벳 공간에 넣어둠
                }
            }else if(elem in 'a'..'z'){
                //열쇠 발견

                key[elem-'a'] = true;//열쇠 획득처리
                visited[nr][nc] = true;//방문처리
                q.offer(arrayOf(nr,nc))
                for(posi:Array<Int> in gates[elem-'a']){//해당 열쇠칸 싹다 방문
                    val openR = posi[0]
                    val openC = posi[1]
                    map[openR][openC] = '.'
                    visited[openR][openC] = true
                    q.offer(arrayOf(openR,openC))
                }
            }else if(elem=='$'){
                //문서 발견

                res++
                visited[nr][nc] = true
                q.offer(arrayOf(nr,nc))
            }else{
                visited[nr][nc] = true
                q.offer(arrayOf(nr,nc))
            }
        }
    }
    return res
}

