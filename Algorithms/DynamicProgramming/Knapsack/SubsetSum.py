class Solution:
    def numIndexPosition(self, target, nums):
        # Special case for target = 0 with multiple zeros
        if target == 0:
            zero_indices = [i for i, num in enumerate(nums) if num == 0]
            if len(zero_indices) >= 2:
                return zero_indices[:2]
            
        dp = {0: []}  # Initialize DP table with sum 0 and empty index list
        for i, num in enumerate(nums):
            current_sums = list(dp.keys())
            for s in current_sums:
                new_sum = s + num
                if new_sum > target or new_sum in dp: # Remove new_sum > target  if the list accepts negative numbers
                    continue
                dp[new_sum] = dp[s] + [i]
                if new_sum == target:
                    return dp[target]  # Early termination when target is reached
        return []  # Return empty list if no solution is found
    


if __name__ == '__main__':
    solution = Solution()
    nums = [7,15,1,5,2,0,0]
    target = 10
    result = solution.numIndexPosition(target, nums)
    print(result)