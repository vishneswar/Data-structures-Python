
class LinkedList:
	"""
	Implementation of sigle linked list
	"""
	def __init__(self):
		"""Inititalizing the list with none"""
		self.head = None
		self.last = None

	def clear(self):
		"""It clears the entire list"""
		current = self.head
		while current:
			prev = current
			current = None
			current = current.next
		self.last = None

	def __len__(self):
		"""This returns the length of the linked list"""
		length = 0
		current = self.head
		while current:
			length += 1
			current = current.next
		return length

	def isEmpty(self):
		"""Checks if the list is empty"""
		if self.head == None:
			return True
		return False

	def add(self, value):
		"""Adds the value at the end of the list"""
		node = self.Node(value)
		if self.head == None:
			self.head = node
			return
		current = self.head

		while current.next:
			current = current.next
		current.next = node	
		self.last = node

	def addFirst(self, value):
		"""Adds the value at the beggining of the list"""
		node = self.Node(value)
		current = self.head
		self.head = node
		node.next = current		

	def peekFirst(self):
		"""Returns the value of the head element"""
		return self.head.data
		
	def peekLast(self):
		"""Returns the value of the tail"""
		return self.last.data

	def removeFirst(self):
		"""Removes the element at the beggining of the list"""
		if not self.head:
			raise Exception("List is empty")
		current = self.head
		value = current.data
		if current.next:
			self.head = current.next
			current = None
		if not self.head.next:
			self.head = None
			self.last = None
		return value
		

	def remove(self, value):
		"""Remove an element if the element is in the list"""
		index = self.indexOf(value)
		if index > 0:
			self.removeAt(index)
		

	def removeAt(self, index):
		"""Remove the element at a particular index"""
		i = 0
		current = self.head
		prev = None
		while current:
			if index == 0:
				self.removeFirst()
				return
			if index == i:
				prev.next = current.next
				if not prev.next:
					self.last = prev
				data = current.data
				return data
			i += 1
			prev = current
			current = current.next
		return IndexError("Index not within the list")
		
		
	def indexOf(self, value):
		"""Returns the position of an element in the list"""
		i = 0
		current = self.head
		while current:
			if current.data == value:
				return i
			i +=1
			current = current.next
		return -1		

	def contains(self, value):
		"""Checks if a value is present in the list"""
		current = self.head
		while current and current.data != value:
			return True
		return False
	
	def __repr__(self):
		"""Returns a string which is a array representation of the Linked list"""
		lst = []	
		current = self.head
		while current:
			lst.append(current.data)
			current = current.next
		
		return str(lst)
	

	class Node:
		"""
		Node class which has data and pointer to the next element in the list
		"""
		def __init__(self, value):
			"""Initialize a node with the given value"""
			self.data = value
			self.next = None