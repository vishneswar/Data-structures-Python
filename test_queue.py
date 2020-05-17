import unittest
from queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_queue(self):
        with self.assertRaises(Exception):
            self.queue.enqueue()
        
        self.queue.enqueue(3)
        self.assertEqual(repr(self.queue), '[3]')
        self.assertEqual(self.queue.dequeue(), 3)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.queue.dequeue()
        self.assertEqual(repr(self.queue), '[4, 5, 6]')


if __name__ == '__main__':
    unittest.main()