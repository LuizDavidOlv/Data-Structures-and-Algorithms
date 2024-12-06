#Source: https://leetcode.com/problems/remove-element/description/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_pointer = 0

        for read_pointer in range(len(nums)):
            if nums[read_pointer] != val:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1

        return write_pointer
    



