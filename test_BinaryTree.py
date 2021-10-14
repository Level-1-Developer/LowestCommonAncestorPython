import unittest
import BinaryTree

class MyTestCase(unittest.TestCase):

    def test_addNode(self):

        node = BinaryTree.Node(5)
        node2 = BinaryTree.Node(10)
        node3 = BinaryTree.Node(2)

        myTree = BinaryTree.BinaryTree()
        myTree.addNode(myTree, node)
        myTree.addNode(myTree, node2)
        myTree.addNode(myTree, node3)

        testCheck = 5
        self.assertEqual(testCheck, myTree.root.data)  # add assertion here
        testCheck = 10
        self.assertEqual(testCheck, myTree.root.rightChild.data)
        testCheck = 2
        self.assertEqual(testCheck, myTree.root.leftChild.data)
        testCheck = None
        self.assertEquals(testCheck, myTree.root.rightChild.rightChild.data)

    def test_lowest_common_ancestor(self):

        myTree = BinaryTree.BinaryTree()
        node = BinaryTree.Node(5)
        node2 = BinaryTree.Node(10)
        node3 = BinaryTree.Node(2)
        node4 = BinaryTree.Node(15)

        myTree.addNode(node)
        myTree.addNode(node2)
        myTree.addNode(node3)
        myTree.addNode(node4)

        testCheck = 5
        result = myTree.lowest_common_ancestor(myTree, node2.data, node3.data)
        self.assertEqual(testCheck, result)

        testCheck = 5
        result = myTree.lowest_common_ancestor(myTree, node2.data, node4.data)
        self.assertEquals(testCheck, result)


if __name__ == '__main__':
    unittest.main()
