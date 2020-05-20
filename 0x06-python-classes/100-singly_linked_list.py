#!/usr/bin/python3
""" Class Node: creates linked list """


class Node:
    """ Create data """
    @property
    def data(self):
        """ returns data """
        return self.__data

    """ Sets a linked list """
    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    """ Return next_node """
    @property
    def next_node(self):
        return self.__next_node

    """ sets next_node """
    @next_node.setter
    def next_node(self, value):
        if value is None:
            self.__next_node = value
            return
        if type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

    """ sets all when creating class """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

""" Class SinglyLinkedList: inner class """


class SinglyLinkedList:
    """ sets head """
    def __init__(self):
        self.__head = None

    """ sets nodes """
    def sorted_insert(self, value):
        temp = self.__head
        new_node = Node(value, self.__head)
        if temp is None:
            self.__head = new_node
            return
        if temp.data > value:
            new_node.next_node = temp
            self.__head = new_node
            return
        while temp.next_node is not None:
            if temp.next_node.data > value:
                break
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
        return

    """ control what gets printed """
    def __str__(self):
        st = ""
        temp = self.__head
        while temp is not None:
            st += str(temp.data)
            if temp.next_node is not None:
                st += '\n'
            temp = temp.next_node
        return st
