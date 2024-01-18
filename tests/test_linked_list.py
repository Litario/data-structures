import pytest

from src.linked_list import Node, LinkedList

node = Node(None)
ll = LinkedList()


## ____________________________________________tests for Node
def test__node_init():
    assert isinstance(node, Node)
    assert node.data is None
    assert node.next_node is None


## ______________________________________tests for LinkedList
def test__init():
    assert ll.head is None
    assert ll.tail is None
    assert ll.data_size == 0
    assert ll.data_list == []


def test__str1():
    assert str(ll) == 'None'


def test__insert_beginning():
    ll.insert_beginning('test1')
    assert ll.head.data == 'test1'
    assert ll.head.next_node is None
    assert ll.tail.data == 'test1'
    assert ll.tail.next_node is None
    assert ll.data_list == ['test1']
    assert ll.data_size == 1

    ll.insert_beginning({'key': 1})
    assert ll.head.data == {'key': 1}
    assert ll.head.next_node.data == 'test1'
    assert ll.tail.data == 'test1'
    assert ll.tail.next_node is None
    assert ll.data_list == [{'key': 1}, 'test1']
    assert ll.data_size == 2


def test__str2():
    assert str(ll) == "{'key': 1} -> test1 -> None"


def test__insert_at_end():
    ll.insert_at_end('test2')
    assert ll.head.data == {'key': 1}
    assert ll.head.next_node.data == 'test1'
    assert ll.head.next_node.next_node.data == 'test2'
    assert ll.tail.data == 'test2'
    assert ll.tail.next_node is None
    assert ll.data_list == [{'key': 1}, 'test1', 'test2']
    assert ll.data_size == 3


def test__str3():
    assert str(ll) == "{'key': 1} -> test1 -> test2 -> None"


def test__to_list():
    ll.insert_at_end({'id': 10, 'username': 'ten'})
    assert ll.to_list() == [{'key': 1}, 'test1', 'test2', {'id': 10, 'username': 'ten'}]


def test__get_data_by_id():
    # with pytest.raises(Exception):
    #     ll.get_data_by_id(100)

    x = ll.get_data_by_id(10)
    assert x == {'id': 10, 'username': 'ten'}
