# class BinaryTree
from Node import *

class BinaryTree():
    def __init__(self, root):
        self.__Root = root

    def getRoot(self):
        return self.__Root

    def isRoot(self, node):
        return node == self.__Root

    #code prof parce que j'avais pas compris la définition de tailleet cherchais à compter les niveaux de l'arbre plutotque les noeuds
    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.getLeft()) + 1 + self.size(node.getRight())

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.getLeft()) + str(node.getVal()) + " " + self.printValues(node.getRight())

    def sumValues(self, node):
        if node is None:
            return 0
        else:
            return self.sumValues(node.getLeft()) + node.getVal() + self.sumValues(node.getRight())

    def numberLeaves(self, node):
        if node is None:
            return 0
        elif node.getLeft() == None and node.getRight() == None:
            return 1
        else:
            return self.numberLeaves(node.getLeft()) + self.numberLeaves(node.getRight())

    def numberInternalNodes(self, node):
        if node == None or (node.getLeft() == None and node.getRight() == None):
            return 0
        else:
            return self.numberInternalNodes(node.getLeft()) + 1 + self.numberInternalNodes(node.getRight())

    def height(self, node, s = -1):
        if node == None:
            return s
        else:
            return max((str(self.height(node.getLeft(), s+1)) + " " + str(self.height(node.getRight(), s+1))).split())







# programme principal

#Je trouve qu'avec cette façon décrire l'arbre il est trop facile de se tromper et j'aime bien que chaque noeud est son"nom" associé pour pouvoir lors de tests ou autre
#BT = BinaryTree(Node(12))
#BT.getRoot().setLeft(Node(5))
#BT.getRoot().setRight(Node(17))
#BT.getRoot().getLeft().setLeft(Node(4))
#BT.getRoot().getLeft().setRight(Node(6))
#BT.getRoot().getLeft().getLeft().setLeft(Node(3))
#BT.getRoot().getRight().setRight(Node(19))
#BT.getRoot().getRight().getRight().setRight(Node(21))
#BT.getRoot().getRight().getRight().setLeft(Node(18))

node18 = Node(18)
node21 = Node(21)
node3 = Node(3)
node19 = Node(19, node18, node21)
node4 = Node(4, node3)
node6 = Node(6)
node5 = Node(5, node4, node6)
node17 = Node(17, None, node19)
node12 = Node(12, node5, node17)
BT = BinaryTree(node12)
print(BT.size(BT.getRoot()))
print(BT.printValues(BT.getRoot()))
print(BT.sumValues(BT.getRoot()))
print(BT.numberLeaves(BT.getRoot()))
print(BT.numberInternalNodes(BT.getRoot()))
print(BT.height(BT.getRoot()))
