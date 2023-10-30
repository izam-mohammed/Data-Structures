
class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
        
    # heapify up
    def _heapify_up(self,i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2
            
    def extract_max(self):
        if not self.heap:
            return
        
        if len(self.heap)==1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, index):
        left_child = 2 * index
        right_child = 2 * index + 1
        largest = index
        
        if (left_child < len(self.heap) and right_child < len(self.heap) and
            self.heap[left_child] > self.heap[right_child]
        ):
            largest = left_child
        
        if (right_child < len(self.heap) and
            self.heap[right_child] > self.heap[largest]
        ):
            largest = right_child
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
            
    def __str__(self) -> str:
        return str(self.heap)

def heap_sort(arr):
    res = list()
    heap = MaxHeap()
    for i in arr:
        heap.insert(i)
    for i in range(len(arr)):
        res.append(heap.extract_max())
    return res
            
            
if __name__ == "__main__":
    ls = [4,2,7,3,6,4,1,8,4]
    hp = MaxHeap()
    for i in ls:
        hp.insert(i)
    print(hp)
    print(hp.extract_max())
    print(hp)
    print(hp.extract_max())
    print(hp)
    
    print(heap_sort(ls))