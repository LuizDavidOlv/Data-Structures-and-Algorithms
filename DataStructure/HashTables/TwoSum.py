# Source: https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        seen: dict[int,int] = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i

if __name__ == '__main__':
    nums = [-1,-2,-3,-4,-5,-6]
    target = -8
    solution = Solution()
    result = solution.twoSumMoreThanOneSum(nums, target)
    if result == [2, 4]:
        print("Passed")
    else:
        print("Failed")


    nums = [3, 3]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [0, 1]:
        print("Passed")
    else:
        print("Failed")


    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [0, 1]:
        print("Passed")
    else:
        print("Failed")
    
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [1, 2]:
        print("Passed")
    else:
        print("Failed")
    
    
    nums = [3, 2, 4]
    target = 7
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [0, 2]:
        print("Passed")
    else:
        print("Failed")
    
    nums = [3, 2, 4]
    target = 5
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [0, 1]:
        print("Passed")
    else:
        print("Failed")
    
    nums = [3, 2, 4]
    target = 3
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == []:
        print("Passed")
    else:
        print("Failed")

    