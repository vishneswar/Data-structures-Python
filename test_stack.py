import unittest
from stack import Stack
class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_stack(self):

        with self.assertRaises(Exception):
            self.stack.pop()
        
        self.stack.push(3)
        self.assertEqual(repr(self.stack), '[3]')
        self.assertEqual(self.stack.pop(), 3)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(6)
        self.stack.pop()
        self.assertEqual(repr(self.stack), '[5, 4, 3]')


if __name__ == '__main__':
    unittest.main()