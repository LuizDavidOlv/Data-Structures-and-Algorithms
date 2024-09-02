# Source: https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linkedList = ListNode()
        currentNode = linkedList
        carry = 0

        while l1 or l2 or carry:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            currentNode.next = ListNode(sum % 10)
            currentNode = currentNode.next
            carry = sum // 10

        return linkedList.next
    
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = solution.addTwoNumbers(l1, l2)
    if result.val == 7 and result.next.val == 0 and result.next.next.val == 8:
        print("Test case 1: Passed")
    else:
        print("Test case 1:Failed")

    # Test case 2
    l1 = ListNode(0)
    l2 = ListNode(0)

    result = solution.addTwoNumbers(l1, l2)
    if result.val == 0:
        print("Test case 2: Passed")
    else:
        print("Test case 2: Failed")

    # Test case 3
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)

    result = solution.addTwoNumbers(l1, l2)
    if result.val == 8 and result.next.val == 9 and result.next.next.val == 9 and result.next.next.next.val == 9 and result.next.next.next.next.val == 0 and result.next.next.next.next.next.val == 0 and result.next.next.next.next.next.next.val == 0:
        print("Test case 3: Passed")
    else:
        print("Test case 3: Failed")
    # Test case 4
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)

    result = solution.addTwoNumbers(l1, l2)
    if result.val == 8 and result.next.val == 9 and result.next.next.val == 9 and result.next.next.next.val == 9 and result.next.next.next.next.val == 1:
        print("Test case 4: Passed")
    else:
        print("Test case 4: Failed")