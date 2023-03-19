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
        
    def test_print_ll(self):
        """
        Тест insert_at_end
        """
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.print_ll(), print("{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"))
