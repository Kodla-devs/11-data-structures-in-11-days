class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
fourthNode = Node(4)

firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode