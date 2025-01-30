# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/1525445863/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        k = 1
        oneIsPresent = False
        listSize = len(nums)
        if listSize <= 1:
            return 0

        for right in range(listSize):
            if nums[right] == 1:
                oneIsPresent = True
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        
        if not oneIsPresent:
            return 0

        return right-left