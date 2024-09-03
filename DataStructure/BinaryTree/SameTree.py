# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = self.checkTreeRecursive(p, q)
        return result
    

    def checkTreeRecursive(self,p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.checkTreeRecursive(p.left, q.left) and self.checkTreeRecursive(p.right, q.right)



if __name__ == '__main__':
    solution = Solution()
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    result = solution.isSameTree(p, q)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    result = solution.isSameTree(p, q)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    result = solution.isSameTree(p, q)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(2), TreeNode(1))
    result = solution.isSameTree(p, q)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(2))
    result = solution.isSameTree(p, q)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(2), TreeNode(2))
    result = solution.isSameTree(p, q)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(2), TreeNode(1))
    result = solution.isSameTree(p, q)
    if result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(2))
    result = solution.isSameTree(p, q)
    if not result:
        print("Test Passed")
    else:
        print("Test Failed")
    
    p = TreeNode(1, TreeNode(2), TreeNode(1))