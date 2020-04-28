#classe Node

class Node:
    def __init__(self, val, left=None, right=None):
        self.__Val = val
        self.__Right = right
        self.__Left = left

    def getVal(self):
        return self.__Val

    def getRight(self):
        return self.__Right

    def getLeft(self):
        return self.__Left

    def setRight(self, R):
        self.__Right = R

    def setLeft(self, L):
        self.__Left = L

    def __str__(self):
        if self.__Left == None and self.__Right == None:
            return str(self.__Val) + " " + "None" + " " + "None"
        elif self.__Left == None:
            return str(self.__Val) + " " + "None" + " " + str((self.__Right).getVal())
        elif self.__Right == None:
            return str(self.__Val) + " " + str((self.__Left).getVal()) + " " + "None"
        return str(self.__Val) + " " + str((self.__Left).getVal()) + " " + str((self.__Right).getVal())


#programme principal

if __name__== '__main__':
    node1 = Node(6)
    print(node1)


