from ListNodeModel import ListNode
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        headDummy = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head.next = head.next.next
                    if head.val != head.next.val:
                        dummy.next = head.next
                        head = head.next
            else:
                head = head.next
                dummy = dummy.next

        return headDummy.next

class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        headDummy = ListNode(0, head)
        dummy = headDummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                dummy.next = head.next
            else:
                dummy = dummy.next
            head = head.next

        return headDummy.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))))
    solution = Solution2()
    result = solution.deleteDuplicates(head)
    if result.val == 1 and result.next.val == 3 and result.next.next.val == 5:
        print("Remove Duplicates from Sorted List II: Passed")