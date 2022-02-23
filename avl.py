# Name: Samuel Kim
# OSU Email: kims6@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Dynamic Array and ADT Implementation
# Due Date: 31 FEB 2022
# Description: Explore writing methods for dynamic array implementation.


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Overrides string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super().str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self.root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object):
        """
        Adds a new node with given value in the tree and auto balances
        """
        n = self.root

        if n is None:
            self.root = AVLNode(value)
            return self.root

        self.add_helper(n, value)

    def add_helper(self, root, value):
        """
        helper method to add nodes
        """
        if not root:
            new_n = AVLNode(value)
            new_n.height = 1
            return new_n
        elif value < root.value:
            root.left = self.add_helper(root.left, value)
            left_root = root.left
            left_root.parent = root
        else:
            root.right = self.add_helper(root.right, value)
            right_root = root.right
            right_root.parent = root

        # Set root height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Rebalance
        return self.rebalance(root)

    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        # This method MUST be re-implemented
        pass

    # ------------------------------------------------------------------ #

    ################################################################
    # It's highly recommended, though not required,
    # to implement these methods for balancing the AVL Tree.
    ################################################################

    def balance_factor(self, n):
        """
        Returns the balance factor of the root node
        """
        if not n:
            return 0

        return self.get_height(n.right) - self.get_height(n.left)

    def update_height(self, n):
        """
        Updates height of input node
        """
        n.height = 1 + max(self.get_height(n.left), self.get_height(n.right))

    def get_height(self, n):
        """
        Returns the height of the node
        """
        if n is None:
            return 0
        return n.height

    def rotate_left(self, n):
        """
        Rotate left about the given node
        """
        c = n.right
        n.right = c.left
        if n.right is not None:
            n.right.parent = n
        c.left = n
        n.parent = c
        self.update_height(n)
        self.update_height(c)
        return c

    def rotate_right(self, n):
        """
        Rotate right about the given node
        """
        c = n.left
        n.left = c.right
        if n.right is not None:
            n.right.parent = n
        c.right = n
        n.parent = c
        self.update_height(n)
        self.update_height(c)
        return c

    def rebalance(self, n):
        """
        Implements rotations if balance is required
        """
        bf = self.balance_factor(n)
        if not n.parent:
            return 0

        # L-R
        if bf < 0:
            if self.balance_factor(n.left) > 0:
                n.left = self.rotate_left(n.left)
                return self.rotate_right(n)
            # L-L
            else:
                return self.rotate_right(n)
        elif bf > 0:
            # R-L
            if self.balance_factor(n.right) < 0:
                n.right = self.rotate_right(n.right)
                return self.rotate_left(n)
            # R-R
            else:
                return self.rotate_left(n)
        else:
            return n

    # ------------------------------------------------------------------ #

    ################################################################
    # Use the methods as a starting point if you'd like to override.
    # Otherwise, the AVL can simply call any BST method.
    ################################################################

    '''
    def contains(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        return super().contains(value)

    def inorder_traversal(self) -> Queue:
        """
        TODO: Write your implementation
        """
        return super().inorder_traversal()

    def find_min(self) -> object:
        """
        TODO: Write your implementation
        """
        return super().find_min()

    def find_max(self) -> object:
        """
        TODO: Write your implementation
        """
        return super().find_max()

    def is_empty(self) -> bool:
        """
        TODO: Write your implementation
        """
        return super().is_empty()

    def make_empty(self) -> None:
        """
        TODO: Write your implementation
        """
        super().make_empty()
    '''


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),  # RR, RR
        (10, 20, 30, 50, 40),  # RR, RL
        (30, 20, 10, 5, 1),  # LL, LL
        (30, 20, 10, 1, 5),  # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        print('INPUT  :', tree, tree.root.value)
        tree.remove(tree.root.value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
