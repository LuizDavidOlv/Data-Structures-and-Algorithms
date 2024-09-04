#Source: https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:          
            if root:
                tempLeft = root.left
                root.left = self.invertTree(root.right)
                root.right = self.invertTree(tempLeft)          
            return root
    

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    result = solution.invertTree(root)
    if result.val == 4:
        print("Test Passed")
    else:
        print("Test Failed")
    
    if result.left.val == 7:
        print("Test Passed")
    else:
        print("Test Failed")
    
    if result.right.val == 2:
        print("Test Passed")
    else:
        print("Test Failed")
    
    if result.left.left.val == 9:
        print("Test Passed")
    else:
        print("Test Failed")
    
    if result.left.right.val == 6:
        print("Test Passed")
    else:
        print("Test Failed")
    
    if result.right.left.val == 3:
        print("Test Passed")
    else:
        print("Test Failed")
    
    if result.right.right.val == 1:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    result = solution.invertTree(root)
    if result.val == 2:
        print("Test Passed")
    else:
        print("Test Failed")
    
    if result.left.val == 3:
        print("Test Passed")
    else:
        print("Test Failed")
    
    if result.right.val == 1:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    result = solution.invertTree(root)
    if result.val == 1:
        print("Test Passed")
    else:
        print("Test Failed")
    
    if result.left.val == 2:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    result = solution.invertTree(root)
    if result.val == 1:
        print("Test Passed")
    else:
        print("Test Failed")
    