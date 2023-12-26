"""Здесь надо написать тесты с использованием unittest для модуля queue."""

from src.queue import Node, Queue

node = Node(None)
queue = Queue()


def test__node_init():
    assert isinstance(node, Node)
    assert node.data == None
    assert node.next_node == None


def test__queue_init():
    assert isinstance(queue, Queue)
    assert queue.head == None
    assert queue.tail == None

def test__queue_str_start():
    assert str(queue) == ""

def test__queue_enqueue():
    assert Queue.queue_data_list == []

    queue.enqueue("data_1")
    assert Queue.queue_data_list == ["data_1"]
    assert queue.head.data == "data_1"
    assert queue.tail.data == "data_1"

    queue.enqueue("data_2")
    assert Queue.queue_data_list == ["data_1", "data_2"]
    assert queue.head.data == "data_1"
    assert queue.head.next_node.data == "data_2"
    assert queue.tail.data == "data_2"

    queue.enqueue("data_3")
    assert Queue.queue_data_list == ["data_1", "data_2", "data_3"]
    assert queue.head.data == "data_1"
    assert queue.head.next_node.data == "data_2"
    assert queue.head.next_node.next_node.data == "data_3"
    assert queue.tail.data == "data_3"

    assert queue.tail.next_node is None


def test__queue_str():
    assert str(queue) == "data_1\ndata_2\ndata_3"
