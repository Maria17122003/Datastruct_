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
        
    def test_to_list(self):
        """
        Тест
        to_list
        """
        self.ll_1 = LinkedList()
        self.ll_1.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll_1.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll_1.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll_1.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(self.ll_1.to_list(), [{'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'},
                                               {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'}])

    def test_get_data_by_id(self):
        """
        Тест
        get_data_by_id
        """
        self.ll2 = LinkedList()
        self.ll2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll2.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll2.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll2.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(self.ll2.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})
        self.assertEqual(self.ll2.get_data_by_id(4), 'Данные не являются словарем или в словаре нет id')

