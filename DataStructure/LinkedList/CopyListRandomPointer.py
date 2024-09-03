#Source: https://leetcode.com/problems/copy-list-with-random-pointer/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        
        return old_to_new[head]

    
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    result = solution.copyRandomList(node1)
    if result.val == 7 and result.next.val == 13 and result.next.next.val == 11:
        print("Test case 1: Passed")
    else:
        print("Test case 1:Failed")

    # Test case 2
    node1 = Node(1)
    node2 = Node(2)

    node1.next = node2
    node1.random = node2
    node2.random = node2

    result = solution.copyRandomList(node1)
    if result.val == 1 and result.next.val == 2:
        print("Test case 2: Passed")
    else:
        print("Test case 2: Failed")

    # Test case 3
    node1 = Node(3)
    node2 = Node(3)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3
    node1.random = node1
    node2.random = node1
    node3.random = node1

    result = solution.copyRandomList(node1)
    if result.val == 3 and result.next.val == 3 and result.next.next.val == 3:
        print("Test case 3: Passed")
    else:
        print("Test case 3: Failed")
