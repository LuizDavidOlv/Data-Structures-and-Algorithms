#Source: https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

from collections import deque

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        queue = deque(nums)
        queue.rotate(k)
        nums[:] = list(queue)
    
if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)
    if nums == [5,6,7,1,2,3,4]:
        print("Rotate Array: Passed")
    else:
        print("Rotate Array: Failed")
    
    nums = [-1,-100,3,99]
    k = 2
    solution.rotate(nums, k)
    if nums == [3,99,-1,-100]:
        print("Rotate Array: Passed")
    else:
        print("Rotate Array: Failed")
    

    nums = [1,2]
    k = 3
    solution.rotate(nums, k)
    if nums == [2,1]: # -> [1,2] -> [2,1] -> [1,2] -> [2,1]
        print("Rotate Array: Passed")
    else:
        print("Rotate Array: Failed")