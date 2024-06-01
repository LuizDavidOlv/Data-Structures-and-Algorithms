#Source https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
nums = [1,1]

def removeElement(self, nums):
    i = 0
    while i< len(nums) -1:
        if nums[i] == nums[i+1]:
            nums.pop(i+1)
        else:
            i += 1
    return len(nums), nums

def removeElement2(self, nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j, nums[:j]
print(removeElement2(removeElement, nums))