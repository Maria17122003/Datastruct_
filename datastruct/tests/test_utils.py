import unittest
from datastruct.datastruct.utils import Stack

stack = Stack()
stack.push("data1")
stack.push("data2")
stack.push("data3")


class Testutils(unittest.TestCase):

    def test_push(self):
        """
        Тест push
        """
        self.assertEqual(stack.top.data, "data3")