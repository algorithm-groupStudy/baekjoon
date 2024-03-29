# Union-Find
> 분리 집합(서로소 집합)  



### 정의  
- 서로 중복되지 않은 부분집합들로 나눠진 원소들에 대한 정보를 저장/조작하는 자료구조
- 전체 집합이 있을 때 구성 원소들이 겹치지 않도록 분할하는데 사용
- 셋(set): 개체들의 집합(순서 고려 x)
- Set A의 모든 원소가 B에 포함되면 - A 는 B의 부분집합, B 는 A 의 초월집합
- 두 집합이 공유하는 원소가 없을 때 mutually disjoint 하다고 한다.
- 분할; 그 합이 원래의 set 이 되어야 하며 서로는 mutually disjoint

### 기능/구현
- make-set(x): x 를 유일한 원소로 하는 set 생성, 정의
- union(x, y): x가 속한 set 과 y가 속한 set 을 병합
- find(x): x가 속한 set의 대표값을 반환

### Union(x, y)
- x, y 가 속한 각각의 set 을 find 로 찾음
- union by size) 원소 수가 적은 set 을 많은 쪽(서브트리)로 합치는 것이 효율적
- union by height) 트리의 높이가 작은 set 을 높은 set 의 서브트리로 합치는 것이 효율적
* 모두 시간복잡도 O(1)

### 구현  
<br/>

```py
#부모 노드의 값을 얻는 함수
def getParent(parents, x):
    if parents[x] == x: return x
    #압축 과정 포함
    p = getParent(parents, parents[x])
    parents[x] = p
    return p

#두 부모 노드를 합치는 함수
def unionParent(parents,x1, x2, cnt):
    a = getParent(parents,x1)
    b = getParent(parents,x2)
    if a != b :
        parents[b] = a
        cnt[a] += cnt[b]

#루트 찾기
def findParent(x, parents):
    if parents[x] == x: return x
    return findParent(parents[x], parents)
```

cf) 이 역시 그리디함을 배제할 수는 없어 재귀의 문제가 발생한다.  
출처 - [분리집합 - 1](https://velog.io/@ashooozzz/Python-%EB%B6%84%EB%A6%AC%EC%A7%91%ED%95%A9-%EC%84%9C%EB%A1%9C%EC%86%8C%EC%A7%91%ED%95%A9) ,  [분리집합 - 2](https://m.blog.naver.com/good5229/221819936100)


cf) MST(Meen Spanning Tree, 최소신장 트리)

출처 - [MST](https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html) 

