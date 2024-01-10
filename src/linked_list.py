class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""
    linked_list_size = 0
    linked_list_data = []

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""

        node = Node(data)
        if self.__class__.linked_list_size == 0:
            self.head = node
            self.tail = node
            self.__class__.linked_list_data.append(self.head.data)
        else:
            curr = self.head
            self.head = node
            self.head.next_node = curr
            self.__class__.linked_list_data.insert(0, self.head.data)

        self.__class__.linked_list_size += 1

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""

        node = Node(data)
        if self.__class__.linked_list_size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

        self.__class__.linked_list_size += 1
        self.__class__.linked_list_data.append(data)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.lstrip()
