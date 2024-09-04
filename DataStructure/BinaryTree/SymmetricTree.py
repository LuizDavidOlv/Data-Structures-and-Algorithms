#Source: https://leetcode.com/problems/symmetric-tree/submissions/1378794273/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.sym(root.left, root.right)

    def sym(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.sym(root1.left, root2.right) and self.sym(root1.right, root2.left)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    result = solution.isSymmetric(root)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    result = solution.isSymmetric(root)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)
    result = solution.isSymmetric(root)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    result = solution.isSymmetric(root)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(6)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(4)
    result = solution.isSymmetric(root)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")