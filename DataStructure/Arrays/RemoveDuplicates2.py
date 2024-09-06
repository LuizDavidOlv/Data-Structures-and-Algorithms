#Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        index = 1
        occurance = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            else:
                occurance = 1

            if occurance <= 2:
                nums[index] = nums[i]
                index += 1
        
        return index
        

if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    nums = [1, 1, 1, 2, 2, 3]
    solution = Solution()
    result = solution.removeDuplicates(nums)
    if result == 5:
        print("Remove Duplicates from Sorted Array II: Passed")
    else:
        print("Remove Duplicates from Sorted Array II: Failed")
    
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    result = solution.removeDuplicates(nums)
    if result == 7:
        print("Remove Duplicates from Sorted Array II: Passed")
    else:
        print("Remove Duplicates from Sorted Array II: Failed")