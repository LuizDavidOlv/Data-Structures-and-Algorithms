#Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional
from ListNodeModel import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next
    
if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    solution = Solution()
    result = solution.removeNthFromEnd(head, n)
    if result == [1, 2, 3, 5]:
        print("Remove Nth Node from End of List: Passed")
    else:
        print("Remove Nth Node from End of List: Failed")