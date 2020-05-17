from dynamic_arrays import DynamicArray
import unittest

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.arr = DynamicArray()
        self.arr.append(1)
        self.arr.append(2)
        self.arr.append(3)
        self.arr.append(4)

    def test_add(self):
        self.assertEqual(len(self.arr), 4)
        self.arr.append(10)
        self.arr.append(10)
        self.arr.append(10)
        self.arr.append(10)
        self.assertEqual(len(self.arr), 8)
        self.assertEqual(self.arr[3], 4)
        self.arr.insertAt(1, 8)
        self.arr.insertAt(1, 'Hello')
        self.assertEqual(self.arr[1], 'Hello')
        self.assertEqual(self.arr[2], 8)
        self.assertEqual(self.arr[10], None)
        

    def test_remove(self):
        self.assertEqual(self.arr.remove(3), 3)
        self.assertEqual(self.arr.removeAt(1), 2)
        self.assertEqual(repr(self.arr), 'DynamicArray([1, 4])')
        

    def test_aux_methods(self):
        self.arr.clear()
        self.assertEqual(repr(self.arr), 'DynamicArray([])')



if __name__ == '__main__':
    unittest.main()