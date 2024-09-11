#Source: https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True

if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,3,3,0,0,4]
    result = solution.canJump(nums)
    print(result)