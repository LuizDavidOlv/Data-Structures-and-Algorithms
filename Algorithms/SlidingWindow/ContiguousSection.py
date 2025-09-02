from collections import defaultdict
from typing import List


class Solution:
    def contiguous_section(self, fruits: List[int], k: int):
        total_contiguous_sections = 0 
        list_size = len(fruits)
        frequency = defaultdict(int)
        pairs = 0
        left = 0

        for right, right_fruit in enumerate(fruits):
            prev = frequency[right_fruit]
            frequency[right_fruit] = prev + 1

            if (prev+1) % 2 == 0:
                pairs += 1
            
            while pairs >= k:
                total_contiguous_sections = list_size - right
                left_fruit = fruits[left]

                if frequency[left_fruit] % 2 == 0:
                    pair -= 1
                
                frequency[left_fruit] -= 1
                left += 1


        return total_contiguous_sections

    
if __name__ == "__main__":
    fruits = [1, 3, 3, 1]
    k = 1
    result = Solution().contiguous_section(fruits, k)
    print(result)



"""
You're an inspector at a large fruit orchard. After harvesting, the fruits are laid out in a long conveyor belt. 
Your job is to identify sections of the conveyor belt that have a significant number of duplicate fruits. 
Specifically, you need to count the number of contiguous sections of the belt where you can form at least k pairs 
of identical fruits based on their position on the belt. 
Each fruit at a specific position can be part of at most one pair when counting towards the k pairs.

Example

For fruits = [0, 1, 0, 1, 0] and k = 2, the output should be solution(fruits, k) = 3.

There are 3 contiguous sections where you can find at least k = 2 pairs of identical fruits:

fruits[0..3] = [0, 1, 0, 1]: One pair of fruit type 0 (at positions 0 and 2) and 
                             one pair of fruit type 1 (at positions 1 and 3).
fruits[1..4] = [1, 0, 1, 0]: One pair of fruit type 1 (at positions 0 and 2 within this section) and 
                             one pair of fruit type 0 (at positions 1 and 3 within this section).
fruits[0..4] = [0, 1, 0, 1, 0]: We can form one pair of fruit type 0 (e.g., at indices 0 and 2) and 
                                one pair of fruit type 1 (at indices 1 and 3). 
                                Note that it is not possible to form both a pair with the 0 at index 0 and the 0 at index 2, 
                                and a pair with the 0 at index 2 and the 0 at index 4, at the same time, 
                                since each fruit can belong to only one pair.

For fruits = [2, 2, 2, 2, 2, 2] and k = 3, the output should be solution(fruits, k) = 1.

There is only 1 applicable contiguous section fruits[0..5] = [2, 2, 2, 2, 2, 2], 
where you can form at least three pairs of fruit type 2 
(e.g., the fruit at position 0 with position 1, position 2 with position 3, and position 4 with position 5).

For fruits = [1, 3, 3, 1] and k = 1, the output should be solution(fruits, k) = 4.

There are 4 contiguous sections where you can find at least k = 1 pair of identical fruits:

fruits[0..2] = [1, 3, 3] (a pair of fruit type 3 at positions 1 and 2)
fruits[0..3] = [1, 3, 3, 1] (a pair of fruit type 3 at positions 1 and 2)
fruits[1..2] = [3, 3] (a pair of fruit type 3 at positions 0 and 1 within this section)
fruits[1..3] = [3, 3, 1] (a pair of fruit type 3 at positions 0 and 1 within this section)
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer fruits

An array of integers representing the sequence of fruits on the conveyor belt.

Guaranteed constraints:
2 ≤ fruits.length ≤ 2000,
0 ≤ fruits[i] ≤ 104.

[input] integer k

A positive integer representing the minimum number of pairs to count.

Guaranteed constraints:
1 ≤ k ≤ fruits.length / 2.

[output] integer

Return the number of contiguous sections which contain at least k pairs of identical fruits.
"""