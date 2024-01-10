"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""

from src.linked_list import Node, LinkedList

node = Node(None)
ll = LinkedList()


## ____________________________________________________tests for Node
def test__node_init():
    assert isinstance(node, Node)
    assert node.data is None
    assert node.next_node is None


## ______________________________________________tests for LinkedList
def test__init():
    assert ll.head is None
    assert ll.tail is None
    assert ll.linked_list_size == 0
    assert ll.linked_list_data == []


def test__str1():
    assert str(ll) == 'None'


def test__insert_beginning():
    ll.insert_beginning('test1')
    assert ll.head.data == 'test1'
    assert ll.head.next_node is None
    assert ll.tail.data == 'test1'
    assert ll.tail.next_node is None
    assert ll.linked_list_data == ['test1']
    assert ll.linked_list_size == 1

    ll.insert_beginning({'key': 1})
    assert ll.head.data == {'key': 1}
    assert ll.head.next_node.data == 'test1'
    assert ll.tail.data == 'test1'
    assert ll.tail.next_node is None
    assert ll.linked_list_data == [{'key': 1}, 'test1']
    assert ll.linked_list_size == 2

def test__str2():
    assert str(ll) == "{'key': 1} -> test1 -> None"


def test__insert_at_end():
    ll.insert_at_end('test2')
    assert ll.head.data == {'key': 1}
    assert ll.head.next_node.data == 'test1'
    assert ll.head.next_node.next_node.data == 'test2'
    assert ll.tail.data == 'test2'
    assert ll.tail.next_node is None
    assert ll.linked_list_data == [{'key': 1}, 'test1', 'test2']
    assert ll.linked_list_size == 3


def test__str3():
    assert str(ll) == "{'key': 1} -> test1 -> test2 -> None"
