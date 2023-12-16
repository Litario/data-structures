from src.stack import Node, Stack

obj_node = Node("data_0")
obj_stack = Stack()


def test__node_init():
    assert isinstance(obj_node, Node)
    assert obj_node.data == "data_0"
    assert obj_node.next_node == None


def test__stack_init():
    assert isinstance(obj_stack, Stack)
    assert obj_stack.top == None
    assert obj_stack.size == 0


def test__stack_push():
    obj_stack.push("data_1")
    assert isinstance(obj_stack.top, Node)
    assert obj_stack.top.data == "data_1"
    assert obj_stack.size == 1

    obj_stack.push("data_2")
    assert isinstance(obj_stack.top, Node)
    assert obj_stack.top.data == "data_2"
    assert obj_stack.size == 2


def test__stack_pop():
    obj_stack.pop()
    assert obj_stack.top.data == "data_1"
    assert isinstance(obj_stack.top, Node)
    assert obj_stack.size == 1
    obj_stack.pop()
    assert obj_stack.top is None
    assert obj_stack.size == 0
    obj_stack.pop()
    assert obj_stack.size == 0
