# Loop Explanation
First Iteration:

* temp = cur.next: temp points to the node immediately after cur.
* cur.next = temp.next: cur skips temp and points to the node after temp.
* temp.next = prev.next: temp is inserted at the beginning of the reversed sublist.
* prev.next = temp: prev now points to temp.


Subsequent Iterations:

The same steps are repeated, effectively moving temp nodes to the beginning of the reversed sublist and adjusting pointers accordingly.
Example

Consider a linked list 1 -> 2 -> 3 -> 4 -> 5 and we want to reverse the sublist from position 2 to 4.

Initial list: 1 -> 2 -> 3 -> 4 -> 5

After first iteration: 1 -> 3 -> 2 -> 4 -> 5

After second iteration: 1 -> 4 -> 3 -> 2 -> 5

