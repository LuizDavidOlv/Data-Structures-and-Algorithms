#Source: https://leetcode.com/problems/count-complete-tree-nodes/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = 1  # Count the current node

        if root.left is not None:
            count += self.countNodes(root.left)
        if root.right is not None:
            count += self.countNodes(root.right)

        return count

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    result = solution.countNodes(root)
    if result == 6:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    result = solution.countNodes(root)
    if result == 7:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    result = solution.countNodes(root)
    if result == 1:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    result = solution.countNodes(root)
    if result == 2:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.right = TreeNode(3)
    result = solution.countNodes(root)
    if result == 2:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = solution.countNodes(root)
    if result == 3:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    result = solution.countNodes(root)
    if result == 4:
        print("Test Passed")
    else:
        print("Test Failed")