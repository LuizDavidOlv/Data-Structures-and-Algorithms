from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len,right-left+1)

        return max_len

class Solution2:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k<0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right-left +1

if __name__ == "__main__":
    solution = Solution2()
    numList = [0,0,1,1,0,1,1,1,1,0,0,0,0,1,1]
    result = solution.longestOnes(numList,2)


    '''
    On Solution2, once it finds the max_len. In this case "0,1,1,0,1,1,1,1", k will be -1 if the next one is zero
    That menas that 
    None
    0,                  0,1,1,0,1,1,1,1,0,0,0,0,1,1
    0,0,                1,1,0,1,1,1,1,0,0,0,0,1,1
    0,0,1,              1,0,1,1,1,1,0,0,0,0,1,1
    0,0,1,1,            0,1,1,1,1,0,0,0,0,1,1
    0,1,1,0,            1,1,1,1,0,0,0,0,1,1
    0,1,1,0,1,          1,1,1,0,0,0,0,1,1
    0,1,1,0,1,1,        1,1,0,0,0,0,1,1
    0,1,1,0,1,1,1,      1,0,0,0,0,1,1
    0,1,1,0,1,1,1,1,    0,0,0,0,1,1
    1,1,0,1,1,1,1,0,    0,0,0,1,1
    1,0,1,1,1,1,0,0,    0,0,1,1
    0,1,1,1,1,0,0,0,    0,1,1
    1,1,1,1,0,0,0,0,    1,1
    1,1,1,0,0,0,0,1,    1
    1,1,0,0,0,0,1,1
    '''