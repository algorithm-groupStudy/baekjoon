class heapSort():
    def __init__(self):
        self.queue = []
    
    def insert(self, n):
        self.queue.append(n)    # 리스트에 추가해주기
        last_index = len(self.queue)-1    # 마지막으로 추가한 요소의 인덱스
        while 0<=last_index:    # 루트까지 탐색
            parent_index = self.parent(last_index)    # 요소의 부모노드 인덱스 찾기
            # 부모노드의 인덱스가 0보다 크거나 같을때, 그리고 부모노드가 현재 요소보다 작을때
            if 0<=parent_index and self.queue[parent_index]<self.queue[last_index]:
                # 서로 위치 교환
                self.swap(last_index, parent_index)
                # 교환 후 마지막 요소가 원래 부모노드에 있는 요소로 바뀌었으므로
                # 변수에 대입 후 다시 반복문 돌리기
                last_index = parent_index

            # 부모노드가 자식노드가 클때까지 반복문 돌리기
            else:
                break    
    
    def swap(self, i ,parent_index): # 위치 바꿔주기
        self.queue[i], self.queue[parent_index] = self.queue[parent_index],self.queue[i]
    
    def parent(self,index): # index의 부모노드 찾기
        return (index-1)//2 

    def leftchild(self,index): # index의 왼쪽 자식노드 찾기
        return index*2+1
    
    def rigtchild(self,index): # index의 왼쪽 자식노드 찾기
        return index*2+2
    
    def printHeap(self):   # 큐 리스트 출력
        print(self.queue)

# 해당 파일 자체에서 실행할 때
# 아래 코드를 실행함
# import시 그 모듈안에 있는 모든 코드들이
# 그대로 실행되는 것을 막기위해 선언
if __name__=="__main__":
    hs=heapSort()
    hs.insert(7)
    hs.insert(2)
    hs.insert(5)
    hs.insert(3)
    hs.insert(4)
    hs.insert(6)
    hs.printHeap()
