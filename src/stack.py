class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    stack_list = []

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.size = 0

    def __repr__(self):
        return f"Длина списка стэка {str(self.size)}"

    def __len__(self):
        return len(Stack.stack_list)

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data)
        node.next_node = self.top
        self.top = node
        self.size += 1
        Stack.stack_list.append(self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top:
            overhead = self.top
            self.top = self.top.next_node
            self.size -= 1
            del Stack.stack_list[-1]
            return overhead.data
        else:
            return None
