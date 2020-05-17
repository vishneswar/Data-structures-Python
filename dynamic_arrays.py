import ctypes

class DynamicArray:
	"""Dynamic Array which can resize based on usage"""
	def __init__(self, capacity=1):
		"""Initailize the array with capactiy 1"""
		self.length = 0
		self.capacity = capacity
		self.array = self.make_array(capacity)

	def __len__(self):
		"""Returns the length of the array"""
		return self.length

	def __getitem__(self, index):
		""""Returns the element at a particular index"""
		try:
			if self.length > index >= 0:
				return self.array[index]
		except:
			 IndexError("Out of bound")

	def __repr__(self):
		"""Returns the representaion of the class"""
		values = ''

		for i in range(self.length):
			values += str(self.array[i]) + ', '

		values = values[: len(values) - 2]
		return "DynamicArray([" + values + "])"

	def append(self, value):
		"""Add value to the end of the array"""
		if self.length == self.capacity:
			self.__re_size()

		self.array[self.length] = value
		self.length += 1

	def removeAt(self, index):
		""""Removes the element from the array if the index is within the range of the array"""
		if self.length < index or index < 0:
			return IndexError("Index out of bound")
		if self.length == 0:
			print("Array is already empty")
			return -1

		value = self.array[index]

		for i in range(index, self.length - 1):
			self.array[i] = self.array[i + 1]

		self.array[self.length - 1] = 0
		self.length -= 1
		self.__re_size()
		return value

	def remove(self, value):
		""""Removes the value if it exits in the array"""
		for i in range(self.length):
			if value == self.array[i]:
				self.removeAt(i)
				return value

		print("Value not found in the array")

	def clear(self):
		"""Clears the entire array"""
		for i in range(self.length):
			self.array[i] = 0

		self.length = 0
		self.__re_size()
		return

	def insertAt(self, index, value):
		"""Inserts the value at a particular index"""
		if self.length < index or index < 0:
			return IndexError("Index out of bound")
		if self.length == self.capacity:
			self.__re_size()

		for i in range(self.length - 1, index - 1, -1):
			self.array[i + 1] = self.array[i]

		self.length += 1
		self.array[index] = value
		return

	def __re_size(self):
		"""private method to dynamically resize the arrya"""
		if self.capacity == self.length:
			temp = self.make_array(2 * self.capacity)
		elif self.capacity == self.length * 4:
			temp = self.make_arrya(self.capacity // 2)
		elif self.length == 0:
			self.array = self.make_array(1)
			return
		else:
			return

		for i in range(self.length):
			temp[i] = self.array[i]
		self.array = temp

		return

	def make_array(self, new_capacity):
		"""Returns the new array with the desired capacity"""
		self.capacity = new_capacity
		return (new_capacity * ctypes.py_object)()