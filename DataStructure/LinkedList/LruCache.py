class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node: ListNode):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add_to_front(self, node: ListNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        

    def move_to_front(self, node: ListNode):
        self.remove_node(node)
        self.add_to_front(node)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.move_to_front(node)
            return node.val

        return -1 


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.move_to_front(node)
        else:
            if len(self.hashmap) >= self.capacity:
                lru_node = self.tail.prev
                self.remove_node(lru_node)
                del self.hashmap[lru_node.key]

            new_node = ListNode(key,value)
            self.add_to_front(new_node)
            self.hashmap[key] = new_node

        

if __name__ == "__main__":
    lru = LRUCache(3)
    get1 = lru.get(2)
    assert get1 == -1

    put1 = lru.put(1,1)
    assert 1 in lru.hashmap
    assert lru.head.next.val == 1
    assert lru.head.val == 0
    assert lru.head.next.prev.val == 0
    assert lru.head.next.next.val == 0
    assert lru.head.next.next.prev.val == 1

    put1 = lru.put(2,2)
    assert 2 in lru.hashmap
    assert 1 in lru.hashmap
    assert lru.head.next.val == 2
    assert lru.head.val == 0
    assert lru.head.next.prev.val == 0
    assert lru.head.next.next.val == 1
    assert lru.head.next.next.prev.val == 2

    get2 = lru.get(1)
    assert 1 in lru.hashmap
    assert 2 in lru.hashmap
    assert lru.head.next.val == 1
    assert lru.head.val == 0
    assert lru.head.next.prev.val == 0
    assert lru.head.next.next.val == 2
    assert lru.head.next.next.prev.val == 1

    put2 = lru.put(3,3)
    assert 1 in lru.hashmap
    assert 3 in lru.hashmap
    assert 2 in lru.hashmap
    assert lru.head.next.val == 3
    assert lru.head.val == 0
    assert lru.head.next.prev.val == 0
    assert lru.head.next.next.val == 1
    assert lru.head.next.next.prev.val == 3
    assert lru.head.next.next.next.val == 2
    assert lru.head.next.next.next.prev.val == 1






        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)