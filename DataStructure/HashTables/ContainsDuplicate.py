# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen_lookup = {}
        for i,num in enumerate(nums):
            if num in seen_lookup and abs(i - seen_lookup[num]) <= k:
                return True 
            seen_lookup[num] = i
        return False


if __name__ == '__main__':
    nums = [2, 8, 9, 3, 10, 1, 4, 11, 12, 4, 1, 1]
    k = 2
    solution = Solution()
    result = solution.containsNearbyDuplicate(nums, k)
    if result:
        print("Passed")
    else:
        print("Failed")

    nums = [1, 0, 1, 1]
    k = 1
    result = solution.containsNearbyDuplicate(nums, k)
    if result:
        print("Passed")
    else:
        print("Failed")

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    result = solution.containsNearbyDuplicate(nums, k)
    if not result:
        print("Passed")
    else:
        print("Failed")