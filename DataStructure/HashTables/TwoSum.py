from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible_solutions = {}
        solution_indexes = []
        for num in nums:
            if num in possible_solutions:
                if num == possible_solutions[num]:
                    solution_indexes = [index for index, value in enumerate(nums) if value == possible_solutions[num]]
                else:
                    solution_indexes.append(nums.index(possible_solutions[num]))
                    solution_indexes.append(nums.index(num))
                return solution_indexes

            possible_solutions[target - num] = num

        return []

if __name__ == '__main__':
    nums = [-1,-2,-3,-4,-5]
    target = -8
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [2, 4]:
        print("Passed")
    else:
        print("Failed")


    nums = [3, 3]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [0, 1]:
        print("Passed")
    else:
        print("Failed")


    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [0, 1]:
        print("Passed")
    else:
        print("Failed")
    
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [1, 2]:
        print("Passed")
    else:
        print("Failed")
    
    
    nums = [3, 2, 4]
    target = 7
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [0, 2]:
        print("Passed")
    else:
        print("Failed")
    
    nums = [3, 2, 4]
    target = 5
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == [0, 1]:
        print("Passed")
    else:
        print("Failed")
    
    nums = [3, 2, 4]
    target = 3
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result == []:
        print("Passed")
    else:
        print("Failed")
    

   
    

    