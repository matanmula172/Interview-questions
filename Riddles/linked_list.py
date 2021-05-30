# Node class
import sys


class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null

    def set_next(self, node):
        self.next = node

    def is_tail_or_head(self):
        return self.data == sys.maxsize


# Linked List class
class LinkedList:

    def __init__(self):
        self.head = Node(sys.maxsize)
        self.tail = Node(sys.maxsize)
        self.head.set_next(self.tail)

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
        return node

    def my_delete(self, node):
        if node is None or node.is_tail_or_head():
            return
        temp = node.next
        node.data = temp.data
        node.next = temp.next