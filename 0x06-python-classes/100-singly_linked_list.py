#!/usr/bin/python3

"""define a class node of a singly linked list"""


class Node:
    """class node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """initializes the private instance attribute
        Args:
            data (int): data of the list_t
            next_node(Node or NULL): node of the list
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the data
        Arg:
            value (int): data to be set
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """value: set the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""define a class SinglyLinkedList"""


class SinglyLinkedList:
    """a class SinglyLinkedList"""
    def __init__(self):
        """initialize  the head"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list
            (increasing order)
        Args:
            value (int): data to be inserted
        """
        new_n = Node(value)
        if self.__head is None:
            new_n.next_node = None
            self.__head = new_n
        elif self.__head.data > value:
            new_n.next_node = self.__head
            self.__head = new_n
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_n.next_node = tmp.next_node
            tmp.next_node = new_n

    def __str__(self):
        """representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
