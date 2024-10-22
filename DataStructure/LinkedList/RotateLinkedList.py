
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k==0:
            return head


        # compute the length to get the last node
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        #Make the list circular
        current.next = head

        #Normalize k
        k = k % length
        # k == 0 means that the will rotate n times and get back to the same place
        if k == 0:
            current.next = None 
            return head
        
        # Find the new tail: (length-k) steps from the beginning
        steps_to_new_tail = length -k 
        new_tail = head
        for _ in range(steps_to_new_tail-1):
            new_tail = new_tail.next
        
        # The new head is next to the new tail
        new_head = new_tail.next
        new_tail.next = None #Make it go back to a non circular list again

        return new_head

   

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next= ListNode(7)
    l1.next.next.next.next = ListNode(9)

    result = solution.rotateRight(l1,2)
    print(result)