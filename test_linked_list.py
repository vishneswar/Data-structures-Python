from linked_list import LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.llist = LinkedList()
        self.llist.add(1)
        self.llist.add(2)
        self.llist.add(3)

    def test_add(self):
        self.llist.addFirst(10)
        self.assertEqual(repr(self.llist), '[10, 1, 2, 3]')
        self.assertEqual(self.llist.last.data, 3)
        self.assertEqual(self.llist.head.data, 10)


    def test_remove(self):
        self.llist.add(4)
        self.llist.add(5)
        self.assertEqual(repr(self.llist), '[1, 2, 3, 4, 5]')
        self.llist.removeFirst()
        self.assertEqual(repr(self.llist), '[2, 3, 4, 5]')
        self.assertEqual(self.llist.head.data, 2)
        self.llist.removeAt(3)
        self.assertEqual(repr(self.llist), '[2, 3, 4]')
        self.llist.remove(3)
        self.assertEqual(repr(self.llist), '[2, 4]')
        self.assertEqual(self.llist.last.data, 4)
        self.assertEqual(self.llist.head.data, 2)
    
    def test_aux_methods(self):
        self.llist.add(4)
        self.llist.add(5)
        self.assertEqual(repr(self.llist), '[1, 2, 3, 4, 5]')
        self.assertEqual(self.llist.indexOf(10), -1)
        self.assertEqual(self.llist.indexOf(1), 0)
        self.assertTrue(self.llist.contains(4))
        self.assertFalse(self.llist.isEmpty())
        self.assertEqual(len(self.llist), 5)

if __name__ == '__main__':
    unittest.main()