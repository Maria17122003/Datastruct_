import unittest
from datastruct.datastruct.linked_list import LinkedList


class Testutils(unittest.TestCase):

    def test_insert_beginning(self):
        """
        Тест insert_beginning
        """
        ll = LinkedList()
        self.assertEqual(ll.insert_beginning({'id': 1}), None)
        self.assertEqual(ll.insert_beginning({'id': 0}), None)

    def test_insert_at_end(self):
        """
        Тест insert_at_end
        """
        ll = LinkedList()
        self.assertEqual(ll.insert_at_end({'id': 2}), None)
        self.assertEqual(ll.insert_at_end({'id': 3}), None)
