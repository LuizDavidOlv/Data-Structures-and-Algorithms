#Source: https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from typing import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = Counter(reversed(nums))
        maxValue = max(count, key=count.get)
        return maxValue



if __name__ == '__main__':
    solution = Solution()
    result = solution.majorityElement([3,2,3])
    if result == 3:
        print("Test Passed")
    else:
        print("Test Failed")
   
