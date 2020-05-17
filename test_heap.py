import unittest
from heap import Heap

class TestHeap(unittest.TestCase):

    def setUp(self):
        self.heap = Heap()
        self.heap.add(10)
        self.heap.add(15)
        self.heap.add(40)
        self.heap.add(100)
        self.heap.add(22)
        self.heap.add(24)
        self.heap.add(42)

    def test_add(self):
        self.heap.add(25)
        self.heap.add(2)
        self.assertEqual(repr(self.heap), '[100, 40, 42, 25, 22, 15, 24, 10, 2]')
        self.assertEqual(len(self.heap), 9)


    def test_remove(self):
        self.assertEqual(self.heap.peek(), 100)
        self.assertEqual(self.heap.remove(), 100)
        self.assertEqual(repr(self.heap), '[42, 40, 24, 10, 22, 15]')
        self.heap.remove()
        self.heap.remove()
        self.heap.remove()
        self.assertEqual(repr(self.heap), '[22, 10, 15]')
        self.heap.remove()
        self.heap.remove()
        self.heap.remove()
        self.heap.remove()
        self.heap.remove()
        self.assertEqual(repr(self.heap), '[]')

if __name__ == '__main__':
    unittest.main()