class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def my_successor(self):
        if self.right is not None:
            temp = self.right
            while temp.left is not None:
                temp = temp.left
            return temp

        p_pointer = self.parent
        temp = self
        while p_pointer is not None:
            if temp != p_pointer.right:
                break
            temp = p_pointer
            p_pointer = p_pointer.parent
        return p_pointer


class Tree:
    def __init__(self, key):
        self.root = Node(key)

    def insert(self, key):
        # 1) If tree is empty then return a new singly node
        if self.root is None:
            self.root = Node(key)
            return self.root
        temp = self.root
        inserted_node = Node(key)
        while True:
            last_node = temp
            if key <= temp.key:
                temp = temp.left
                if temp is None:
                    last_node.left = inserted_node
                    inserted_node.parent = last_node
                    return inserted_node
            else:
                temp = temp.right
                if temp is None:
                    last_node.right = inserted_node
                    inserted_node.parent = last_node
                    return inserted_node


def zizag_traversal(root):
    # Base Case
    tree_arr = []
    lvl_arr = []
    if root is None:
        return

    # Create two stacks to store current and next level
    current_level = []
    next_level = []

    # order to of print
    left_to_right = True

    # append root to current level stack
    current_level.append(root)

    # Check if stack is empty
    while len(current_level) > 0:
        # Pop from stack
        temp = current_level.pop(-1)
        # Print the data
        # print(temp.key, end=" ")
        lvl_arr.append(temp.key)

        if left_to_right:
            if temp.left:
                next_level.append(temp.left)
            if temp.right:
                next_level.append(temp.right)
        else:
            if temp.right:
                next_level.append(temp.right)
            if temp.left:
                next_level.append(temp.left)

        if len(current_level) == 0:
            # Reverse order and swap the stacks
            left_to_right = not left_to_right
            current_level, next_level = next_level, current_level
            tree_arr.append(lvl_arr)
            lvl_arr = []
    return tree_arr


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
print(zizag_traversal(root))
