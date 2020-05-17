from linked_list import LinkedList

class Stack:
	"""
	Implementation of stack with linked list
	"""
	def __init__(self):
		self.llist = LinkedList()

	def push(self, value):
		self.llist.addFirst(value)

	def pop(self):
		return self.llist.removeFirst()
	
	def peek(self):
		return self.llist.peekFirst()

	def __len__(self):
		return len(self.llist)
	
	def isEmpty(self):
		return self.llist.isEmpty()

	def __repr__(self):
		return self.llist.__repr__()