# Source 
    https://www.geeksforgeeks.org/what-is-linked-list/

# Definition
    Linked List is a linear data structure, in which elements are not stored at a contiguous location, rather they are linked using pointers.
    It forms a series of connected nodes, where each node stores the data an the address of the next node.

# Structure
    Node: In a linked list a node cosists on:
        Data: it holds the actual value or data associated with the node
        Next Pointer: It stores the memory address of the next node in the sequence
        Head and Tail: The linked list is accessed through the dead node, which points to the first node in the list. 
        The last node in the list points to NULL or nullprt, indicating the end of the list. This node is also known as the tail node.

# Advantages
    Dynamic Data structure: 
        The size of memory can be allocated or de-allocated at run time based on the operation insertion or deletion.

    Ease of Insertion/Deletion: 
        The insertion and deletion of elements are simpler than arrays since no elements need to be shifted after insertion and deletion,
        Just the address needed to be updated.
    
    Efficient Memory Utilization: 
        Linked List is a dynamic data structure. The size increases or decreases as per the requirement so this avoids the wastage of memory
    
    Implementation:
        Various advanced data structures can ve implemented using a linked list like a stack, queue, graph, hash maps, etc.
