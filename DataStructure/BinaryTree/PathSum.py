#Source: https://leetcode.com/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTargetSum(self, root: TreeNode, targetSum: int, currentSum: int) -> bool:
        if root:
            currentSum += root.val
            if currentSum == targetSum and not root.left and not root.right:
                return True
            
            return self.findTargetSum(root.left, targetSum, currentSum) or self.findTargetSum(root.right, targetSum, currentSum)
            


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currentSum = 0
        return self.findTargetSum(root, targetSum, currentSum) 


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    result = solution.hasPathSum(root, 5)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = solution.hasPathSum(root, 5)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(-2)
    root.right = TreeNode(-3)
    result = solution.hasPathSum(root, -5)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = solution.hasPathSum(root, 1)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = solution.hasPathSum(root, 3)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = solution.hasPathSum(root, 6)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = solution.hasPathSum(root, 7)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = solution.hasPathSum(root, 8)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")