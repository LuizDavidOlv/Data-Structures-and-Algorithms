class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)-1
        answer = []
        answer.append(1)

        for i in range(numsLength):
            prefix = answer[i]*nums[i]
            answer.append(prefix)
        
        r = 1

        for i in range(numsLength, -1, -1):
            suffix = answer[i] * r
            answer[i] = suffix
            r = r * nums[i]
        
        return answer