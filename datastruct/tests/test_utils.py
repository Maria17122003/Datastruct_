import unittest
from datastruct.datastruct.utils import Stack

stack = Stack()
stack.push("data1")
stack.push("data2")
stack.push("data3")
data = stack.pop()


class Testutils(unittest.TestCase):

    def test_push(self):
        """
        Тест push
        """
        self.assertEqual(stack.top.data, "data2")

    def test_pop(self):
        """
        Тест pop
        """
        self.assertEqual(data, "data3")
