#Source: https://leetcode.com/problems/remove-element/description/
nums = [2,3,2,3]
val = 3

def removeElement(self, nums, val):
    numsTemp = []
    for i in range(len(nums)):
        if nums[i] != val:
            numsTemp.append(nums[i])
    nums = numsTemp
    return len(nums), nums

def removeElement2(self, nums, val):
    while True:
        if val in nums:
            nums.remove(val)
        else:
            break
    return len(nums), nums
        
print(removeElement2(removeElement, nums, val))