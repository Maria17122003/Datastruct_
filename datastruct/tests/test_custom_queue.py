import unittest
from datastruct.datastruct.custom_queue import Queue


class Testutils(unittest.TestCase):

    def test_enqueue(self):
        """
        Тест enqueue
        """
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, "data1")

    def test_dequeue(self):
        """
        Тест dequeue
        """
        queue1 = Queue()
        queue1.enqueue('data1')
        self.assertEqual(queue1.dequeue(), "data1")
        self.assertEqual(queue1.dequeue(), None)

