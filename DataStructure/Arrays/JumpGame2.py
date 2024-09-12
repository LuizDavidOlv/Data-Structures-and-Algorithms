#source: https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0

        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            
            near = far + 1
            far = farthest
            jumps += 1
        
        return jumps

if __name__ == '__main__':
    solution = Solution()
    nums = [7,0,9,6,9,6,1,0,9,0,1,2,9,0,3]
    result = solution.jump(nums)
