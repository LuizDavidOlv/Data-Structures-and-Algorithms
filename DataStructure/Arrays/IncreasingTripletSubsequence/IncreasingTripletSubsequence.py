class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        listLen = len(nums)
        firstNum = float('inf')
        secondNum = float('inf')
        if listLen < 3:
            return False
        for i in range(0,listLen):
            if nums[i] <= firstNum:
                firstNum = nums[i]
            elif nums[i] <= secondNum:
                secondNum = nums[i]        
            else:
                return True
            
        
        return False
        