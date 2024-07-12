#https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150

from typing import Optional


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Two pointers approach
    def hasCycle(self, head: Optional[Node]) -> bool:
        fast = head
        while(fast and fast.next):
            head = head.next
            fast = fast.next.next
            if head == fast:
                return True
        return False
    
    # Hash Table approach
    def hasCycle2(self, head: Optional[Node]) -> bool:
        visited_nodes = set()
        current_node = head
        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next
        return False

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.head = Node(50)
    linked_list.head.next = Node(20)
    linked_list.head.next.next = Node(15)
    linked_list.head.next.next.next = Node(4)
    linked_list.head.next.next.next.next = Node(10)

    # Create a loop for testing
    linked_list.head.next.next.next.next.next = linked_list.head.next.next

    result = linked_list.hasCycle(linked_list.head)
    print(result)

