#Source: https://leetcode.com/problems/summary-ranges?envType=study-plan-v2&envId=top-interview-150
class SlidingWindowSolution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result_list = []
        range_from = 0
        window_size = 0
        while range_from + window_size < len(nums):
            if range_from + window_size == len(nums) - 1 or nums[range_from + window_size] + 1 != nums[range_from + window_size + 1]:
                result_list.append(str(nums[range_from]) + ("" if window_size == 0 else "->" + str(nums[range_from + window_size])))
                range_from = range_from + window_size + 1
                window_size = 0
            else :
                window_size += 1
        return result_list

class Solution2:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if nums == []:
            return []

        output = []
        i=0
        while i< len(nums):
            start = nums[i] #store initial value of i
            while i+1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i+=1
            
            if start == nums[i]:
                output.append(f"{start}")
            else:
                output.append(f"{start}->{nums[i]}")
            
            i+=1
        
        return output

if __name__ == '__main__':
    solution = Solution2()
    nums = [0,2,3,4,6,8,9]
    result = solution.summaryRanges(nums)
    print(result)

