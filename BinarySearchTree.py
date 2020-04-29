#class BinarySearchTree
from BinaryTree import *

class BinarySearchTree(BinaryTree):

    def __init__(self, root):
        BinaryTree.__init__(self, root)

    def contains(self, node, value):
        if node is None:
            return 0
        elif node.getVal() == value and self.isRoot(node):
            return True
        elif node.getVal() == value:
            return 1
        else:
            return (self.contains(node.getLeft(), value) + self.contains(node.getRight(), value)) > 0

    def findMin(self, node):
        return min((self.infixe(node)).split())

    def findMax(self, node):
        return max((self.infixe(node)).split())

    def insert(self, node, value):
        if node.getVal() > value:
            if node.getLeft() == None:
                node.setLeft(Node(value))
                return "Done"
            return self.insert(node.getLeft(), value)
        elif node.getVal() < value:
            if node.getRight() == None:
                node.setRight(Node(value))
                return "Done"
            return self.insert(node.getRight(), value)

    def equivalentsBST(self, node1, node2):
        return (BinarySearchTree(node1)).infixe(node1) == (BinarySearchTree(node2)).infixe(node2)



# programme principal
node14 = Node(14)
node6 = Node(6)
node13 = Node(13, None, node14)
node1 = Node(1)
node7 = Node(7, node6)
node15 = Node(15, node13)
node0 = Node(0, None, node1)
node3 = Node(3)
node12 = Node(12, node7, node15)
node2 = Node(2, node0, node3)
node20 = Node(20, node12)
node4 = Node(4, node2, node20)
BT = BinarySearchTree(node4)
print(BT.infixe(BT.getRoot()))
print(BT.contains(BT.getRoot(), 17))
print(BT.findMin(BT.getRoot()))
print(BT.insert(BT.getRoot(), 8))
print(BT.parcoursLargeur(BT.getRoot()))
print(BT.equivalentsBST(node4, node4))


