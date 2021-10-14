#Going to try and translate java to python
#what can go wrong

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def addNode(self, node):
        return self.addNodeMethod(self.root, node.data)

    def addNodeMethod(self, data):

        root = self

        if root == 0:
            root = Node(data)
            return root

        if data > root.data:
            root.rightChild = self.addNodeMethod(root.rightChild, data)
        else:
            root.leftChild = self.addNodeMethod(root.leftChild, data)

        return root

    def lowest_common_ancestor(self, a, b):
        while self.root is not None:
            if self.root.data > a and self.root.data > b: self.root = self.root.leftChild
            elif self.root.data < a and self.root.data < b: self.root = self.root.rightChild
            else: break

        return self.root

myTree = BinaryTree()
myNode = Node(5)

myTree.addNode(myNode)
myTree.addNode(Node(2))
myTree.addNode(Node(8))

print(myTree.lowest_common_ancestor(2,8))