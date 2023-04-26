import java.io.*;
import java.util.*
import kotlin.collections.ArrayDeque

class Node(var priority:Int, var str:String):Comparable<Node>{
    override fun compareTo(o:Node):Int{
        //우선순위 같으면 사전순
        if(this.priority == o.priority){
            return this.str.compareTo(o.str)
        }

        //기본적으로 우선순위 순
        return this.priority-o.priority
    }

    override fun toString():String{
        return this.str
    }
}

var br = BufferedReader(InputStreamReader(System.`in`))


var N=0
var map = HashMap<String,MutableList<String>>()
var inner = HashMap<String,Int>()

fun main(){


    N = br.readLine().toInt()

    //위상정렬 기본 재료 세팅
    var st : StringTokenizer
    for(i in 0 until N){
        st = StringTokenizer(br.readLine())
        var lowItem = st.nextToken()//하위템
        var highItem = st.nextToken()//상위템


        //인접 리스트 작성
        map.putIfAbsent(lowItem, mutableListOf())//하위템 노드 없으면 생성
        map.putIfAbsent(highItem,mutableListOf())//상위템 노드 없으면 생성
        map.get(lowItem)!!.add(highItem)//하위템 인접 정점으로 상위템 등록

        //진입차수 설정
        inner.putIfAbsent(lowItem,0)//없으면 0
        inner.putIfAbsent(highItem,0)//없으면 0
        inner[highItem] = inner[highItem]!!+1//상위템 진입차수 +=1
    }

    print(bfs())
}

fun bfs():String{//위상정렬 영어로 뭐임
    var q = ArrayDeque<Node>()
    val pq = PriorityQueue<Node>()

    //진입차수 0인애들큐에 넣기
    for(key in inner.keys){
        if(inner[key]==0){
            q.add(Node(0,key))
        }
    }



    //큐순회시작
    //큐에서 뽑고
    //pq에 넣는다
    //인접 노드순회
    //차수 1씩 줄인다
    //차수 0이면 큐에 넣는다
    while(!q.isEmpty()){
        var size = q.size
        while(size-->0){
            var cur:Node = q.removeFirst()//현재 아템
            pq.offer(cur)//출력용 pq에 넣다


            val curItem = cur.str//현재 아템
            val curPriority = cur.priority//현재 출력순위

            for(nextItem in map[curItem]!!){
                var nextInner = inner[nextItem]!!//인접아이템의 현재 차수
                inner[nextItem] = nextInner-1//진입차수갱신

                //
                if(inner[nextItem]==0){
                    q.add(Node(curPriority+1,nextItem))
                }
            }
        }
    }
    if(pq.size<map.size){
        return "-1"
    }

    val sb = StringBuilder()
    while(!pq.isEmpty()){
        sb.append(pq.poll().str)
        sb.append("\n")
    }
    return sb.toString()
}