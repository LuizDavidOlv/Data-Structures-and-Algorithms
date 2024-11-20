#Source: https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        listSize = len(nums)

        # until a zero value is found, left and right will be equal
        # if a zero value apears, left will not increase
        # this means that in the next iteration, the left value will be zero
        # the swap will occur and zero will be on the right
        for right in range(listSize):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        listSize = len(nums)

        # as i traverse the array, write will keep constant until num is not zero
        # This will make sure that all non zero integers are placed first
        for i in range(listSize):
            if nums[i] != 0:
                # place non zero value after the last non zero value 
                nums[write] = nums[i]
                write += 1

        # after traversin the array the left over value will still be wrong
        # That is why it is needed to force them to become zero
        nums[write:] = [0] * (listSize-write)


if __name__ == '__main__':
    solution = Solution1()
    inputList = [7,1,0,3,12] 
    result = solution.moveZeroes(inputList)