##### Source: https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150

# Key Concepts
## Hasing for Constant-Time Operations
- Purpose: To achieve O(1) time complexity for insert and remove operations, it requires a way to check the presence of an element and access it quickly
- Implementation: Use a hash table(HashMap or HashSet) to store the elements. This allows you to insert and remove elements in constant time because hash tables provide O(1) average time complexity for these operations.

## Array or List for Random Access
- Purpose: The getRandom method requires selecting a random element uniformly from the current set. Arrays or list provide O(1) time access to elements by index, which is essential for efficient random selection.
- Implementation: Maintain a dynamic array that stores the elements. This allows to pick a random index and retrieve the element at that index in constant time.

## Synchronization of Data Structures
- Challange: Maintaining both a hash table and an array can lead to inconsistencies if not manages carefully, especially during deletion.
- Solution: Ensure that both data structures are updated simultaneously during insert and remove operations.

## Efficient Deletion from Array
- Problem: Removing an element from the middle of an array or list is an O(n) operation because it requires shifting elements
- Solution: To delete an element in O(1) time, swap the element to be removed with the last element in the array and then remove the last element. This method avoids shifting elements and maintains the order of the other elements as non-essential, given that the set is unordered.

## Mapping elements to their indices
- Purpose: To efficiently locate the index of an element in the array during deletion.
- Implementation: use the hash table to store not just the presence of elements but also their indices in the array. This way, you can quickly find the position of any element in the array when you need to remove it.

## Space Complecity Considerations
- Trade-offs: Using both a hash table and an array increases space usage. However, this is acceptable for achieving the required time complexity.

