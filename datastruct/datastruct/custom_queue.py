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
        self.next = None


class Queue:
    def __init__(self, head=None, tail=None):
        """
        Атрибуты, хранящие
        ссылки на начало
        и конец очереди.
        """
        self.head = head
        self.tail = tail

    def enqueue(self, value):
        """
        Добавляет данные
        в очередь
        """
        new_node = Node(data=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
