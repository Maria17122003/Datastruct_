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


class Stack:
    """
    Класс стек
    """

    def __init__(self):
        """
        Атрибут, который хранит
        ссылку на следующий
        узел
        """
        self.top = None

    def push(self, data):
        """
        Добавляет данные
        в стек
        """
        next_node = Node(data)
        next_node.next = self.top
        self.top = next_node

    def pop(self):
        """
        Удаляет из стека
        верхний элемент,
        возвращает данные удаленного
        экземпляра класса Node
        """
        remove = self.top
        self.top = self.top.next
        return remove.data
