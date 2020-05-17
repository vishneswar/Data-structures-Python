import unittest
from binary_search_tree import BinarysearchTree

class TestBST(unittest.TestCase):

    def setUp(self):
        self.bst = BinarysearchTree()

    def test_add(self):
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(70)
        self.bst.add(60)
        self.bst.add(30)
        self.bst.add(1)
        self.bst.add(50)
        self.bst.add(25)
        self.bst.add(72)
        self.bst.add(64)
        self.bst.add(37)
        self.bst.add(11)
        self.assertEqual(repr(self.bst), '[1, 10, 11, 20, 25, 30, 37, 50, 60, 64, 70, 72]')
    
    def test_remove(self):
        self.bst.add(10)
        self.bst.add(20)
        self.bst.add(70)
        self.bst.add(60)
        self.bst.add(30)
        self.bst.add(1)
        self.bst.add(50)
        self.bst.add(25)
        self.bst.add(72)
        self.bst.add(64)
        self.bst.add(37)
        self.bst.add(11)
        self.assertTrue(self.bst.remove(10))
        self.bst.remove(64)
        self.bst.remove(65)
        self.assertEqual(repr(self.bst), '[1, 11, 20, 25, 30, 37, 50, 60, 70, 72]')

    def test_aux(self):
        self.assertEqual(len(self.bst), 0)
        self.bst.add(10)
        self.assertEqual(len(self.bst), 1)
        self.bst.add(20)
        self.bst.add(70)
        self.bst.add(60)
        self.bst.add(30)
        self.bst.add(1)
        self.assertEqual(self.bst.getHeight(), 5)
        self.assertEqual(len(self.bst), 6)


if __name__ == '__main__':
    unittest.main()