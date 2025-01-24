#https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        list_size = len(nums)
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, list_size):
            current_sum += nums[i] - nums[i-k]
            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum/k
    


if __name__ == '__main__':
    solution = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    result = solution.findMaxAverage(nums,k)
    print(result)