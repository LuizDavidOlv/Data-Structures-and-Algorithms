
from xml.dom import Node

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def createBinaryTree(tree, root):
    if root is None:
        return
    tree.append(root.value)
    createBinaryTree(tree, root.left)
    createBinaryTree(tree, root.right)
  


def height(root):
  # Time complexity: O(n)
  # Space complexity: O(h) where h is the height of the tree

  if root is None:
    return -1

  left_height = height(root.left)
  right_height = height(root.right)

  maxValue = max(left_height, right_height) + 1
  return maxValue

def levelOrder(root, result = "", begin = True):
    if begin:
        result += root.value.__str__() + " "

    if root is None:
        return result
    
    if root.left is not None:
        result += root.left.value.__str__() + " "
    if root.right is not None:
        result += root.right.value.__str__() + " "
    result = levelOrder(root.left, result, False)
    result = levelOrder(root.right, result, False)
    return result


my_tree = Node(1)
# my_tree.left = Node(2)
# my_tree.left.left = Node(4)
# my_tree.left.right = Node(5)
my_tree.right = Node(2)
my_tree.right.right = Node(5)
my_tree.right.right.left = Node(3)
my_tree.right.right.right = Node(6)
my_tree.right.right.left.right = Node(4)
level = levelOrder(my_tree)
print( f"Level order traversal: {level}")
# tree_height = height(my_tree)
# print(f"Height of the tree: {tree_height}")


