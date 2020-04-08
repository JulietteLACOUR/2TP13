# class BinaryTree
from Node import *

class BinaryTree():
    def __init__(self, root):
        self.__Root = root

    def getRoot(self):
        return self.__Root

# programme principal
N3 = Node(3)
N18 = Node(18)
N21 = Node(21)
N4 = Node(4, N3)
N6 = Node(6)
N19 = Node(19, N18, N21)
N5 = Node(5, N4, N6)
N17 = Node(17, None, N19)
N12 = Node(12, N5, N17)
BinaryTree1 = BinaryTree(N12)

