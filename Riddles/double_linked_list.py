# Node of a doubly linked list
import sys


class Node:
    def __init__(self, data):
        self.next = None  # reference to next node in DLL
        self.prev = None  # reference to previous node in DLL
        self.data = data

    def set_next(self, node):
        self.next = node

    def set_prev(self, node):
        self.prev = node

    def is_tail_or_head(self):
        return self.data == sys.maxsize


# Linked List class
class DoubleLinkedList:

    def __init__(self):
        self.head = Node(sys.maxsize)
        self.tail = Node(sys.maxsize)
        self.head.set_next(self.tail)
        self.tail.set_prev(self.head)

    def print_list(self):
        temp = self.head.next
        while not temp.is_tail_or_head():
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        node.set_prev(self.head)
        return node

    def my_delete(self, node):
        if node is None or node.is_tail_or_head():
            return
        temp = node.next
        node.data = temp.data
        node.next = temp.next
        temp.prev = None


l = DoubleLinkedList()
x = l.push(1)
l.push(2)
l.push(3)
l.print_list()
l.my_delete(x)
l.print_list()
