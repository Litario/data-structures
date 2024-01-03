"""Здесь надо написать тесты с использованием unittest для модуля queue."""

from src.queue import Node, Queue

node = Node(None)
queue = Queue()


def test__node_init():
    assert isinstance(node, Node)
    assert node.data is None
    assert node.next_node is None


def test__queue_init():
    assert isinstance(queue, Queue)
    assert queue.head is None
    assert queue.tail is None


def test__queue_str_0():
    assert str(queue) == ""


def test__queue_enqueue():
    assert Queue.queue_data_list == []
    assert queue.head is None

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


def test__queue_str_1():
    assert str(queue) == "data_1\ndata_2\ndata_3"


def test__queue_dequeue():
    assert queue.dequeue() == 'data_1'
    assert queue.head.data == "data_2"
    assert queue.head.next_node.data == "data_3"
    assert Queue.queue_data_list == ["data_2", "data_3"]

    assert queue.dequeue() == 'data_2'
    assert queue.head.data == "data_3"
    assert queue.head.next_node is None
    assert Queue.queue_data_list == ["data_3"]

    assert queue.dequeue() == 'data_3'
    assert Queue.queue_data_list == []
    assert queue.dequeue() is None


def test__queue_str_2():
    assert str(queue) == ""
