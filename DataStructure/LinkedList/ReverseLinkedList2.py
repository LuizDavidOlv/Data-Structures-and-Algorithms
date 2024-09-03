#Source: https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        linkedList = ListNode()
        linkedList.next = head
        prev = linkedList

        for i in range(left-1):
           prev = prev.next
        
        cur = prev.next
        for i in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return linkedList.next
       
    
   
    
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    left = 1
    right = 4

    result = solution.reverseBetween(l1, left, right)

    if result.val == 4 and result.next.val == 3 and result.next.next.val == 2 and result.next.next.next.val == 1:
        print("Test case 1: Passed")
    else:
        print("Test case 1: Failed")
    
    
    # Test case 3
    l1 = ListNode(3)
    l1.next = ListNode(5)
    l1.next.next = ListNode(7)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(10)
    l1.next.next.next.next.next = ListNode(27)
    l1.next.next.next.next.next.next = ListNode(8240)
    left = 3
    right = 6
    result = solution.reverseBetween(l1, left, right)
    if result.val == 3 and result.next.val == 5 and result.next.next.val == 27 and result.next.next.next.val == 10 and result.next.next.next.next.val == 9 and result.next.next.next.next.next.val == 7 and result.next.next.next.next.next.next.val == 8240:
        print("Test case 3: Passed")
    else:
        print("Test case 3: Failed")
