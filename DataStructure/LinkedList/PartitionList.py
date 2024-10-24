from typing import Optional
from ListNodeModel import ListNode, Node


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head


        while head:
            if head.val >= x:
                after.next = head
                after = after.next
            else:
                before.next = head
                before = before.next

            head = head.next
        
        after.next = None
        before.next = after_head.next
        
        return before_head.next

if __name__ == '__main__':
    linked_list = ListNode()

    linked_list.head = Node(50)
    linked_list.head.next = Node(20)
    linked_list.head.next.next = Node(15)
    linked_list.head.next.next.next = Node(4)
    linked_list.head.next.next.next.next = Node(10)

    solution = Solution()
    result = solution.partition(linked_list.head,15)