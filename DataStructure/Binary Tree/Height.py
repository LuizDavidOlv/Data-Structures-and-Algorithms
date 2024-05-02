from CreateBinaryTree import CreateTree


def height(root):
  # Time complexity: O(n)
  # Space complexity: O(h) where h is the height of the tree

  if root is None:
    return -1

  left_height = height(root.left)
  right_height = height(root.right)

  maxValue = max(left_height, right_height) + 1
  return maxValue



my_tree = CreateTree()
tree_height = height(my_tree)
print(f"Height of the tree: {tree_height}")


