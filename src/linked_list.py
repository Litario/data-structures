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

    def __init__(self):
        self.head = None
        self.tail = None
        self.data_size = 0
        self.data_list = []

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""

        node = Node(data)
        if self.data_size == 0:
            self.head = node
            self.tail = node
            self.data_list.append(self.head.data)
        else:
            curr = self.head
            self.head = node
            self.head.next_node = curr
            self.data_list.insert(0, self.head.data)

        self.data_size += 1

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""

        node = Node(data)
        if self.data_size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

        self.data_size += 1
        self.data_list.append(data)

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

    def to_list(self):
        return self.data_list

    # def get_data_by_id(self, value):
    #     KEY_NAME = 'id'
    #     for i in self.data_list:
    #         try:
    #             if i.get(KEY_NAME) == value:
    #                 return i
    #         except TypeError:
    #             print('Данные не являются словарем или в словаре нет id.')
    #         except Exception:
    #             print('Данные не являются словарем или в словаре нет id.')

    def get_data_by_id(self, value):
        KEY_NAME = 'id'
        for i in self.data_list:
            if isinstance(i, dict):
                try:
                    if i.get(KEY_NAME) == value:
                        return i
                except TypeError:
                    print('В словаре нет указанного id.')
            else:
                print('Данные не являются словарем.')
