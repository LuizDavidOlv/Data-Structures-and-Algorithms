from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float('inf')
        current_sum = 0
        start = 0

        for end in range(n):
            current_sum += nums[end]
            # Shrink the window as small as possible while the sum is >= target
            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1

        return 0 if min_length == float('inf') else min_length


if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,2,4,3]
    target = 14
    result = solution.minSubArrayLen(target, nums)
    print(result)