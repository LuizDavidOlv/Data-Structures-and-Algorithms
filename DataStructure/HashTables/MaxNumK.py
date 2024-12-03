#https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/1468748481/?envType=study-plan-v2&envId=leetcode-75

#* Two pointer solution on TwoPointers folder

from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = defaultdict()
        operations =0

        for num in nums:
            complement = k - num

            if counts[complement] > 0:
                operations += 1
                counts[complement] -= 1
            else:
                counts[nums] += 1
        
        return operations
