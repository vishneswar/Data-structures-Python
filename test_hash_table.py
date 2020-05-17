from hash_table import HashTable
import unittest

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.ht = HashTable()
        self.ht.add(1, 'hello')
        self.ht.add(2, 'hi')
        self.ht.add(3, 'how')
        self.ht.add('foo', 'are')
        self.ht.add(5, 'foo')
        self.ht.add(36, 'bar')
        self.ht.add('a', 'baz')

    def test_add(self):
        self.assertEqual(self.ht[1], 'hello')
        self.assertEqual(self.ht[3], 'how')
        self.assertEqual(self.ht['foo'], 'are')
        self.assertEqual(self.ht['a'], 'baz')
        self.ht.add(1, 'Modified')
        self.assertEqual(self.ht[1], 'Modified')
        self.assertEqual(self.ht.getSize(), 7)
        self.assertEqual(self.ht.getCapacity(), 12)

        
    def test_remove(self):
        self.assertEqual(self.ht.remove(1), True)
        self.assertIsNone(self.ht[1])
        self.assertEqual(self.ht.remove('ab'), False)

    def test_aux_methods(self):
        self.assertEqual(self.ht.getSize(), 7)
        self.assertEqual(self.ht.getCapacity(), 12)
        self.ht.add(55, 'foo')
        self.ht.add(1, 'bar')
        self.ht.add('random', 'baz')
        self.assertEqual(self.ht.getSize(), 9)
        self.assertEqual(self.ht.getCapacity(), 24)


if __name__ == '__main__':
    unittest.main()