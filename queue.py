from linked_list import LinkedList

class Queue:
    
    def __init__(self):
        self.llist = LinkedList()

    def enqueue(self, value):
	    self.llist.add(value)

    def dequeue(self):
        return self.llist.removeFirst()
	
    def peek(self):
        return self.llist.peekFirst()

    def __len__(self):
        return len(self.llist)
	
    def isEmpty(self):
        return self.llist.isEmpty()

    def __repr__(self):
        return self.llist.__repr__()