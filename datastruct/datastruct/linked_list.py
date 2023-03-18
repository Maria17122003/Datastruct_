class Node:
    """
    Класс узла
    """
    def __init__(self, data):
        """
        Атрибутуты данные и
        ссылка на следующий узел
        """
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, head=None, tail=None):
        """
        Атрибуты, хранящие
        ссылки на начало
        и конец списка.
        """
        self.head = head
        self.tail = tail

    def insert_beginning(self, data):
        """
        Принимает данные, добавляет
        узел с этими данными
        в начало связанного списка
        """
        new_node = Node(data=data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Принимает данные, добавляет
        узел с этими данными
        в конец связанного списка
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            node.next_node = new_node

    def print_ll(self):
        """
        Вывод данных
        """
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)
