#https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/1468748481/?envType=study-plan-v2&envId=leetcode-75



from typing import List

#* Hash Map solution on HashTables folder
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        count = 0

        while left < right:
            current_sum = nums[left]+nums[right]
            if  current_sum == k:
                count += 1
                left += 1
                right -= 1
            else:
                if current_sum > k:
                    right -= 1
                else:
                    left += 1
        
        return count