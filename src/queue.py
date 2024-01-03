class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""
    queue_list = []
    queue_data_list = []

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        self.__class__.queue_data_list.append(data)

        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            current_data_head = self.head.data
            self.head = self.head.next_node
            del self.__class__.queue_data_list[0]
            return current_data_head

            ## вариант без лишней переменной
            # self.head = self.head.next_node
            # return self.__class__.queue_data_list.pop(0)



    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return '\n'.join(self.__class__.queue_data_list)
