class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# def createBinaryTreeTest(tree, root):
#     if root is None:
#         return
#     tree.append(root.value)
#     createBinaryTree(tree, root.left)
#     createBinaryTree(tree, root.right)


def CreateTree():
    my_tree = Node(1)
    my_tree.right = Node(2)
    my_tree.right.right = Node(5)
    my_tree.right.right.left = Node(3)
    my_tree.right.right.right = Node(6)
    my_tree.right.right.left.right = Node(4)
    return my_tree