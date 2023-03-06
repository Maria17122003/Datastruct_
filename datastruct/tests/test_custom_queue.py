import unittest
from datastruct.datastruct.custom_queue import Queue


queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')


class Testutils(unittest.TestCase):

    def test_enqueue(self):
        """
        Тест enqueue
        """
        self.assertEqual(queue.head.data, "data1")
