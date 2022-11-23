class Node():
    """
    A Node class to contain data and direction for the minHeap structure.
    Nodes provide attributes for data, left pointers, right pointers, and parent pointers.
    Also contains inorder, preorder, and postorder traversal methods.
    """
    def __init__(self, data):
        """
        Required Attribute: data to be store in the node
        Initialized to point to None for left, right, and parent
        No return statement
        """
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def inorder(self):
        """
        Traverses tree nodes In Order
        No arguments
        No return statement
        """
        if self.left is not None:
            self.left.preorder()
        print(str(self.data))
        if self.right is not None:
            self.right.preorder()

    def preorder(self):
        """
        Traverses tree nodes Pre Order
        No arguments
        No return statement
        """
        print(str(self.data))
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        """
        Traverses tree nodes Post Order
        No arguments
        No return statement
        """
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
        print(str(self.data))

class MinHeap():
    """
    Minimum Heap Class for efficient storing of ordered information in such a way that
    the lowest value in the data structure can be accessed in constant time.
    Ordered so that the lower values are "higher" up the tree than larger values.
    No required arguments
    No return statement
    """
    def __init__(self):
        """
        Attributes: a root node and the size of the tree (the number of nodes it contains)
        No arguments
        No return statement
        """
        self.root = None
        self.size = 0

    def inorder(self):
        """
        Calls the root node's In Order method to traverse
        No arguments
        No return statement UNLESS the tree is empty
        """
        if self.size == 0:
            return None
        self.root.inorder()

    def preorder(self):
        """
        Calls the root node's Pre Order method to traverse
        No arguments
        No return statement UNLESS the tree is empty
        """
        if self.size == 0:
            return None
        self.root.preorder()

    def postorder(self):
        """
        Calls the root node's Post Order method to traverse
        No arguments
        No return statement UNLESS the tree is empty
        """
        if self.size == 0:
            return None
        self.root.postorder()

    def pop(self):
        """
        Returns and removes the minimum value from the heap.
        If the heap is empty, returns None.
        """
        if self.size == 0:
            return None

        if self.size == 1:
            rtn_value = self.root.data
            self.root = None
            self.size -= 1
            return rtn_value

        rtn_value = self.root.data

        path = self.find_path_to(self.size)
        current_node = self.root

        for direction in path:
            if direction == "0" and current_node.left is not None:
                current_node = current_node.left
            if direction == "1" and current_node.right is not None:
                current_node = current_node.right

        current_node.data, self.root.data = self.root.data, current_node.data

        if current_node.parent.left == current_node:
            current_node.parent.left = None
        else:
            current_node.parent.right = None

        self.bubble_down()

        self.size -= 1
        return rtn_value

    def peek(self):
        """
        Return but do not remove the minimum value of the heap.
        If the heap is empty, returns None.
        """
        if self.size == 0:
            return None
        else:
            return self.root.data


    def insert(self, data):
        """
        Insert the provided data onto the heap.
        Support integers and strings.
        Parameters: Data to insert
        No return statement
        """
        new_node = Node(data)

        if self.size == 0:
            self.root = new_node
        elif self.size == 1:
            new_node.parent = self.root
            self.root.left = new_node
            self.bubble_up(self.root.left)
        elif self.size > 1:
            path = self.find_path_to(self.size+1)
            current_node = self.root

            for direction in path:
                if direction == "0" and current_node.left is not None:
                    current_node = current_node.left
                if direction == "1" and current_node.right is not None:
                    current_node = current_node.right

            if current_node.left == None:
                current_node.left = new_node
                new_node.parent = current_node
            elif current_node.right == None:
                current_node.right = new_node
                new_node.parent = current_node

            current_node = new_node
            self.bubble_up(current_node)

        self.size += 1


    def clear(self):
        """
        Removes all elements from the heap.
        No parameters
        No return statement
        """
        self.root = None
        self.size = 0


    def find_path_to(self, index):
        """
        bitstring method to find a path to a given node
        Parameter: Index of the node to find the path to
        Return: the path to the given node in bitstring
        """
        path = f"{index:b}"
        return path[1:]


    def bubble_down(self):
        """
        Method to "bubble down" the root node to its place by value in the heap.
        No Parameters
        No Return Statement
        """
        current_node = self.root

        while current_node.left is not None or current_node.right is not None:
            if current_node.right is None:
                if current_node.data > current_node.left.data:
                    current_node.data, current_node.left.data = current_node.left.data, current_node.data
                    current_node = current_node.left
            else:
                if current_node.left.data < current_node.right.data:
                    current_node.data, current_node.left.data = current_node.left.data, current_node.data
                    current_node = current_node.left
                else:
                    current_node.data, current_node.right.data = current_node.right.data, current_node.data
                    current_node = current_node.right


    def bubble_up(self, current_node):
        """
        Method to "bubble up" the root node to its place by value in the heap.
        Parameter: node to bubble up
        No Return Statement
        """
        while current_node.parent is not None:
            if current_node.data < current_node.parent.data:
                current_node.data, current_node.parent.data = current_node.parent.data, current_node.data
            else:
                return

            current_node = current_node.parent
