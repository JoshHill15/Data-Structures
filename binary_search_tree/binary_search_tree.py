
# from dll_queue import Queue
# from dll_stack import Stack
# import sys
# sys.path.append('../queue_and_stack')
from collections import deque
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes
        # for us to call `insert` on them
        if value < self.value:
          # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTree(value)
        # otherwise, value >= self.value
        else:
            # check if self.right is a valid node
            if self.right:
                self.right.insert(value)
                # right side empty
            else:
                # found parking spot
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            if target > self.value:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def depth_first_iterative_for_each(self, cb):
        # depth first: stack
        stack = []
        # add the root of the tree to the stack
        stack.append(self)
        # loop so long as the stack still has elements
        while len(stack) > 0:
            current_node = stack.pop()
            # check if right child exists
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)
            # check if the left child exists
            # DAY 2 Project -----------------------

    def breadth_first_iterative_for_each(self, cb):
        # breadth first: queue
        q = deque()
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)

    def map(self, cb, arr=[]):
        val = cb(self.value)
        if self.left:
            self.left.map(cb)
        if self.right:
            self.right.map(cb)
        arr.append(val)
        return arr

        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value),
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(self)
        while q.len() > 0:
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
            print(current.value)

            # Print the value of every node, starting with the given node,
            # in an iterative depth first traversal

    def dft_print(self, node):
        print(node.value)
        if node.left:
            self.dft_print(node.left)
        if node.right:
            self.dft_print(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


binary = BinarySearchTree(5)
binary.insert(50)
binary.insert(1)
binary.insert(14)
binary.insert(-3)
binary.insert(4)
binary.insert(75)

# print(binary.contains(80))
# print(binary.get_max())
binary.in_order_print(binary)
# binary.bft_print(binary)
# binary.dft_print(binary)


def multiplyByTen(num):
    return num * 10


def printVal(x):
    # print(x)
    return x


# print(binary.for_each(multiplyByTen))
# print(binary.for_each(printVal))
# print(binary.depth_first_iterative_for_each(printVal))
# print(binary.breadth_first_iterative_for_each(printVal))
# print(binary.map(printVal))
