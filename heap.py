
class Heap:
    """
    Implementaion of Heap Ds
    """
    def __init__(self):
        """Initialize the heap with a empty array"""
        self.heap = []

    def __len__(self):
        """Returns the length of the heap"""
        return len(self.heap)

    def __parent(self, i):
        """Returns the parent of the node"""
        return i // 2 - 1
    
    def __child(self, i):
        """Returns the child of the node"""
        return (2 * i + 1, 2 * i + 2)

    def add(self, value):
        """Add a element to the heap"""
        self.heap.append(value)
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.maxHeapify(i)

    def peek(self):
        """Returns the maximum element in the heap"""
        if len(self.heap) > 0:
            return self.heap[0]
        return IndexError("Heap is empty")
    
    def remove(self):
        """Removes the max element from the heap"""
        value = self.peek()
        if not isinstance(value, int):
            return
        
        self.heap[0] = self.heap[len(self.heap) - 1]
        del self.heap[len(self.heap) - 1]
        self.maxHeapify(0)
        return value

    def maxHeapify(self, i):
        """Heapify method which maintins the max heap invariant"""
        largest = i
        left, right = self.__child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)
        

    def __repr__(self):
        """"Returns the string representaion of the heap"""
        return str(self.heap)