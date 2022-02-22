# Name: Samuel Kim
# OSU Email: kims6@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: BST/AVL
# Due Date: 21 FEB 2022
# Description: BST Tree Implementation
import queue
import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Overrides string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self.str_helper(self.root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self.str_helper(node.left, values)
        self.str_helper(node.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds new value to the tree. Duplicate values should be added to the right subtree
        """
        p = None
        n = self.root
        if n is None:
            self.root = BSTNode(value)

        else:
            while n is not None:
                p = n
                if value < n.value:
                    n = n.left
                else:
                    n = n.right
            if value < p.value:
                p.left = BSTNode(value)
            else:
                p.right = BSTNode(value)

    def findios(self, start):
        """
        Finds and returns the inorder successor
        """
        output = start.right
        outputp = start
        while output.left:
            outputp = output
            output = output.left
        return outputp, output

    def remove(self, value: object) -> bool:
        """
        Removes value node from the tree and returns True is removed, returns false is nothing is removed
        """
        if self.contains(value):
            pn, n = self.findpn(value)

            #Value is a leaf node
            if n.left is None and n.right is None:
                if n is not self.root:
                    if pn.left == n:
                        pn.left = None
                    else:
                        pn.right = None
                else:
                    if n.value == value:
                        self.root = None

            #Value has two children
            elif n.left and n.right:
                ps, s = self.findios(n)
                if ps == n:
                    s.left = n.left
                    pn.left = s
                else:
                    s.left = n.left
                    ps.left = s.right
                    s.right = n.right
                    if ps.right is n:
                        ps.right = s
                    else:
                        ps.left = s

            #Value has only one child
            else:
                if n.left:
                    ref = n.left
                else:
                    ref = n.right

                if n is not self.root:
                    if n == pn.left:
                        pn.left = ref
                    else:
                        pn.right = ref
                else:
                    self.root = ref
            return True
        else:
            return False

    def contains(self, value: object) -> bool:
        """
        Returns True if value is in tree, otherwise returns False
        """
        n = self.root
        while n is not None:
            if n.value == value:
                return True
            elif value < n.value:
                n = n.left
            else:
                n = n.right
        return False

    def findpn(self, value: object):
        """
        Returns node and parent node
        """
        p = self.root
        n = self.root
        while n is not None:
            if n.value == value:
                return p, n
            elif value < n.value:
                p = n
                n = n.left
            else:
                p = n
                n = n.right

    def inorder_traversal(self) -> Queue:
        """
        Returns a Queue object that contains inorder nodes.
        """
        output = Queue()

        if self.root is None:
            return output
        else:
            self.iot_helper(self.root, output)
            return output

    def iot_helper(self, n, output):
        """
        Helper method for inorder_traversal
        """
        if n.left is not None:
            self.iot_helper(n.left, output)
        output.enqueue(n.value)
        if n.right is not None:
            self.iot_helper(n.right, output)


    def find_min(self) -> object:
        """
        Returns the lowest value in the tree
        """
        n = self.root

        if n is None:
            return None
        else:
            while n.left is not None:
                n = n.left
            return n.value

    def find_max(self) -> object:
        """
        Returns the highest value in the tree
        """
        n = self.root
        if n is None:
            return None
        else:
            while n.right is not None:
                n = n.right
            return n.value

    def is_empty(self) -> bool:
        """
        Returns True if tree is empty and False if otherwise
        """
        if self.root is None:
            return True
        else:
            return False

    def make_empty(self) -> None:
        """
        Removes all nodes from the tree
        """
        self.root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        print('INPUT  :', tree, tree.root.value)
        tree.remove(tree.root.value)
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
