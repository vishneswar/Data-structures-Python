import ctypes
from linked_list import LinkedList

class HashTable:
    """
    Implementaion of Hashtable by chaining with Linked list
    """
    def __init__(self):
        """Initializing the hashtable with a capcity of '3' and load factor of '0.60'"""
        self.DEFAULT_CAPACITY = 3
        self.LOAD_FACTOR = 0.60
        self.capacity = 0
        self.size = 0
        self.table = self.makearray(self.DEFAULT_CAPACITY)

    def hashFunction(self, a, capacity):
        """A simple hash function. If int is passed in it mods the int value and if strings
        are passed, it adds the ascii value of the each char and then mods it over capacity"""
        if type(a) == str:
            temp = a
            a = 0

            for i in temp:
                a += ord(i)

        return a % capacity
        

    def add(self, key, value):
        """Adds the key value pair to the hash table"""
        hash = self.hashFunction(key, self.capacity)
        value = [key, value]

        try:
            liList = self.table[hash]
            index = self.__containsKey(liList, key)

            if index >= 0:
                self.__removeFromLinkedList(liList, index)
            liList.add(value)

        except ValueError:
            self.table[hash] = None
            liList = LinkedList()
            liList.add(value)
            self.table[hash] = liList

        self.size += 1

        if self.size / self.capacity > self.LOAD_FACTOR:
            self.__resizing()

        return True
        

    def remove(self, key):
        """Removes a particular element from the table if it exists"""
        hash = self.hashFunction(key, self.capacity)

        try:
            liList = self.table[hash]
            index = self.__containsKey(liList, key)
            if index < 0:
                return False
            
            self.__removeFromLinkedList(liList, index)

        except ValueError:
            print("Key does not exist in the hash table")
            return False

        return True

    def __containsKey(self, liList, key):
        """Private method that checks if the key is present in the table and returns the
        position of the key in the linked list"""
        current = liList.head
        i = 0

        while current:

            if current.data[0] == key:
                return i

            i +=1
            current = current.next
        
        return -1

    def __removeFromLinkedList(self, liList, index):
        """Private method that removes the element with the given position of the element
        in the linked list"""
        current = liList.head
        self.size -= 1

        if index == 0:

            if current.next: 
                liList.head = current.next
                return

            liList.head = None
            return

        prev = None

        while index != 0:
            prev = current
            current = current.next
            index -= 1

        prev.next = current.next
        current.data = None
        current = None
        

    def __getitem__(self, key):
        """returns the value of the given key"""
        hash = self.hashFunction(key, self.capacity)

        try:
            liList = self.table[hash] 
            current = liList.head

            while current:

                if key == current.data[0]:
                    return current.data[1]

                current = current.next

        except ValueError:
            pass
        print("Key does not exist in hash table")

    def __resizing(self):
        """Private method that resizes the hastable when it reaches the threshold limit"""
        self.capacity *= 2
        oldArray = self.table
        self.table = self.makearray(self.capacity)
        self.size = 0

        for i in range(len(oldArray)):

            try:
                item = oldArray[i].head

                while item:
                    self.add(item.data[0], item.data[1])
                    item = item.next

            except ValueError:
                pass

    def __repr__(self):
        """Returns the index and key value pair of all the elements in the hash table"""
        tabledata = ''

        for i in range(self.capacity):

            try:
                item = self.table[i].head

                while item:
                    tabledata += "\tIndex: " + str(i) + "\tValues: " + str(item.data) + ",\n"
                    item = item.next

            except ValueError:
                pass

        tabledata = "HashTable: { \n" + tabledata + "}"

        return tabledata

    def getSize(self):
        """Returns the size of the hash table"""
        return self.size
    
    def getCapacity(self):
        """Returns the capacity of the hash table"""
        return self.capacity

    def makearray(self, capacity):
        """Returns a new array with the capacity passed in"""
        self.capacity = capacity

        return (capacity * ctypes.py_object)()

