#classe Node

class Node:
    def __init__(self, val, left = None, right = None):
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

#programme principal


