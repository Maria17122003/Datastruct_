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
        next_node = Node(data=value)
        if self.head is None:
            self.head = next_node
            self.tail = next_node
        else:
            self.tail.next_node = next_node
            self.tail = next_node

    def dequeue(self):
        """
        Удаляет из очереди
        крайний левый элемент
        """
        if self.head is None:
            return None
        else:
            dequeue_element = self.head
            self.head = self.head.next_node
            return dequeue_element.data
