class BinarysearchTree:
    """ 
    Binary search tree implementation with insert and delete
    """
    def __init__(self):
        """Initialising root to none"""
        self.root = None
        self.tempList = []
        self.noOfNodes = 0

    def add(self, value):
        """Method to add value into the BST"""
        node = self.Node(value)
        self.noOfNodes += 1
        if not self.root:
            self.root = node 
            return
        self.__insert(self.root, node)

    def __insert(self, root, node):
        """Private helper method which calls it recursively to enter values into the tree"""
        value = node.data
        if value < root.data:
            if not root.left:
                root.left = node
            else:
                self.__insert(root.left, node)
        elif value > root.data:
            if not root.right:
                root.right = node
            else:
                self.__insert(root.right, node)

    def remove(self, value):
        """Remove a value from the tree if it exits"""
        if self.isPresent(value):
            node = self.__deleteNode(self.root, value)
            self.noOfNodes -= 1
            return True
        return False

    def __deleteNode(self, root, value):
        """Helper method which calls itself recursively to delete a element"""
        if not root:
            return
        if value > root.data:
            root.right = self.__deleteNode(root.right, value)
        elif value < root.data:
            root.left = self.__deleteNode(root.left, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp

            if not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.findMin(root.right)
            root.data = temp.data
            root.right = self.__deleteNode(root.right, temp.data)

        return root

    def findMin(self, root):
        """Find the min element conneced to the node passed to the method"""
        while root.left:
            root = root.left
        return root

    def isPresent(self, value):
        """Checks if a value is present in the tree"""
        root = self.root
        while True:
            if not root:
                return False
            if root.data > value:
                root = root.left
            elif root.data < value:
                root = root.right
            else:
                return True

    def getchild(self, node):
        """ Returns a tuple of the left and the right child"""
        return node.left, node.right

    def isLeaf(self, node):
        """Checks if a node is the leaf"""
        if not node.left and not node.right:
            return True
        return False

    def getHeight(self):
        """Returns the height of the tree"""
        return self.__getHeight(self.root)

    def __getHeight(self, root):
        """Helper method to calulate height of the tree"""
        if not root:
            return 0
        return max(self.__getHeight(root.left), self.__getHeight(root.right)) + 1

    def __len__(self):
        """Retruns the number of nodes in the tree"""
        return self.noOfNodes

    def inorderTraversal(self, root):
        """Inorder tree traversal"""
        if root:
            self.inorderTraversal(root.left)
            value = root.data
            self.tempList.append(value)
            self.inorderTraversal(root.right)


    def __repr__(self):
        """Prints the tree in a sorterd format by calling the inorder traversal method"""
        self.inorderTraversal(self.root)
        val = self.tempList[:]
        self.tempList = []
        return str(val)
        

    class Node:
        """Node class"""
        def __init__(self, value):
            """Instantiate a node with the value passed"""
            self.data = value
            self.parent = None
            self.left = None
            self.right = None